from fastapi import FastAPI
import uvicorn
'''Как запустить FastAPI в Docker контейнере'''
app = FastAPI()

@app.get("/users")
async def get_users():
    ...
    return [{"id": 1, "name": "Artem"}]


if __name__ == "__main__":
    uvicorn.run("les_9:app", host="0.0.0.0", port=8000)

# все в файле Dockerfile