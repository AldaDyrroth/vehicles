import requests
import pytest
import random
from datetime import timedelta
from src.api.constant import Par
from typing import Dict, Any
from faker import Faker
from src.data_models.models import VehicleData


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(Par.HEADERS.value)

    return session

@pytest.fixture()
def rndm_vehicle_id():
    session = requests.Session()
    response = session.get(f"{Par.BASE_URL.value}/stock")
    assert response.status_code == 200, "Ошибка авторизации, статус код не 200"

    get_booking = response.json()
    id = random.choice(get_booking)["id"]
    return id
