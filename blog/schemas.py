from fastapi import FastAPI
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str

class User(BaseModel):
    username:str
    email:str
    password:str
