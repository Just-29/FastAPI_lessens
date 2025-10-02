from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

'''Как тестировать API на Python | Pytest + FastAPI'''
# Юнит тест. Остальное в tests\test_api.py
app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Ассинхронность в Python",
        "autor": "Мэтью",
    },
    {
        "id": 2,
        "title": "Backend в Python",
        "autor": "Артем",
    },
]
