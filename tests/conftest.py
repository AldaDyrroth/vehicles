import requests
import pytest

from src.enums.api_enums import Endpoint


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(Endpoint.HEADERS.value)

    return session

