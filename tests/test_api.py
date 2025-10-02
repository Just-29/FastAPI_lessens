import pytest
from httpx import AsyncClient, ASGITransport
import asyncio
# Для запуска тестирования прописать в терминале "pytest -s", "-v" чтоб было удобнее считывать
# Это два интеграционных теста
# Есть юнит тесты, которые не импортят ничего и работают сами по себе 

from les_2 import app

@pytest.mark.asyncio
async def test_get_book():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        respones = await ac.get("/books")
        assert respones.status_code == 200

        data = respones.json()
        assert len(data) == 2

@pytest.mark.asyncio
async def test_post_book():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        respones = await ac.post("/books", json={
            "title": "Nazvanie",
            "author": "Author"
        })
        assert respones.status_code == 200

        data = respones.json()
        assert data == {"success": True, "message": "Книга успешно добавлена"}