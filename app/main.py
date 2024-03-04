from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    name: str
    password: int

@app.post("/register")
async def register_user(user: User):
    