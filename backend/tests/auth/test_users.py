import asyncio
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from tortoise.contrib.test import initializer

from auth.models import User
from sugoi_chat.main import create_app

pytestmark = pytest.mark.asyncio


@pytest.fixture(scope="module")
def app():
    initializer(["auth.models"], db_url='postgres://sugoi:sugoi@localhost:5432/test_sugoi')
    yield create_app()


@pytest.fixture
async def client(app) -> Generator:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


async def test_create_user(client):  # nosec
    response = await client.post("/users", json={"username": "admin", "password": "test"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == "admin"
    assert "id" in data
    user_id = data["id"]

    user_obj = await User.get(id=user_id)
    assert user_obj.id == user_id


async def test_list_users(client: TestClient, event_loop: asyncio.AbstractEventLoop):  # nosec
    response = await client.get("/users")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == "admin"
    assert "id" in data
    user_id = data["id"]

    user_obj = await User.get(id=user_id)
    assert user_obj.id == user_id
