from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel, Field, EmailStr, ConfigDict
#для валидации данных, для внесения ограничений, задать email, для запрета лишней инфы

app = FastAPI()

data = {
    "email": "abc@mail.com",
    "bio": None,
    "age": 12,
}

data_two = {
    "email": "abc@mail.com",
    "bio": "This is a bio",
    "gender": "male",
    "birhday": "2000",
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)

    model_config = ConfigDict(extra="forbid") # Если входящие данные содержат поля, которых нет в модели — будет ошибка

users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"OK": True, "massege": "Добавлен"}

@app.get("/users")
def get_users():
    return users

class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)

user = UserSchema(**data)
#print(repr(user))
#print(UserSchema(**data_two))