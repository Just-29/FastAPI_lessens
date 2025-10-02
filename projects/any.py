from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Users(BaseModel):
    name: str
    surname: str
    age: int
    address: str
    phone_number: str

