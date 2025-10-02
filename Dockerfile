FROM python:3.12.1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "les_10.py"]

# docker build -t my_firs_image. для запуска
# docker build -t для запуска. my_firs_image имя образа. "." говорит что мы находимся втой же дирректории

# docker image чтоб посмотреть все образы
# docker run -p 1252:8000 my_firs_image для запуска образа где my_firs_image имя выбранного созданного образа
# -p это порты. 1252 это порт на компе который может быть любой. 8000 это порт который указан в les_9.py
# docker run --name=my_first_container my_firs_image использовав --name=my_first_container задаем имя образу
# docker exec -it my_first_conteiner зайти в docker контейнер где my_first_conteiner имя контейнера