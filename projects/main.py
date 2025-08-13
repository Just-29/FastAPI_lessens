from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    age: int
    address: str
    phone_number: str

class UserResponse(User):
    id: int

users_db: List[User] = []

@app.post("/users/", response_model=UserResponse)
async def create_user(user: User):
    user_id = len(users_db) + 1
    user_data = user.dict()
    user_data["id"] = user_id
    users_db.append(user_data)
    return user_data

@app.get("/users/", response_model=List[UserResponse])
async def get_all_users():
    return users_db

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    if user_id < 1 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id - 1]

@app.get("/")
async def root():
    return {"message": "User Management System"}