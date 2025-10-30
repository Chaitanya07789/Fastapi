from fastapi import FastAPI , Depends
import schemas, model
from database import engine , SessionLocal ,get_db
from sqlalchemy.orm import Session
import uvicorn

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

@app.post("/blog")
def create_blog(request:schemas.Blog, db:Session = Depends(get_db)):
    new_blog = model.Blog(title=request.title, body=request.body )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blogs")
def get_all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs

@app.post("/user")
def create_user(request:schemas.User, db:Session = Depends(get_db)):
    new_user = model.User(username=request.username, email=request.email, password= request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/user")
def get_all_user(db:Session=Depends(get_db)):
    users = db.query(model.User).all()
    return users


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

