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
def all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

