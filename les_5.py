from fastapi import FastAPI, HTTPException, Response, Depends
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

'''Авторизация на FastAPI — Регистрация и Аутентификация пользователей'''
app = FastAPI()


config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = "cookies"

security = AuthX(config=config)


class UserLoginShema(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(creds: UserLoginShema, response: Response):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"accec_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")


@app.get("/protected", dependencies=[Depends(security.access_token_required)])
def protected():
    return {"data": "TOP secret"}