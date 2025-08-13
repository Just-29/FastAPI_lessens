from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get(path="/", summary="даем название ручке", tags=["вписываем тег"])
def home():
    return {"message": "Hello World!"}


'''три способа запустить fastapi
1) fastapi dev "имя файла"

2) uvicorn "название исполняемого файла без расширения":app --reload

если в коде прописана эта функция
if __name__ == "__main__":
    uvicorn.run(app, reload=True) reload для автоматического обновления. В функции множество параметров
то можно запустить 
3) python "название файла с расширением"
'''