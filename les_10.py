from fastapi import FastAPI
import uvicorn

'''Как задеплоить FastAPI на сервер – Полный гайд'''
app = FastAPI

@app.get("/users", tags=["Пользователи"], summary="получить пользователей")
async def get_users():
    return [{"id": 1, "name": "Artem"}]


if __name__ == "__main__":
    uvicorn.run("les_10:app", host="0.0.0.0", port=8000)