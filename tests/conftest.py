import pytest
import requests
from uuid import uuid4

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

@pytest.fixture(scope="session")
def token():
    token = 'ваш_токен_от_яндекс_диска'
    if not token:
        pytest.fail("YANDEX_TOKEN не установлен в переменных окружения")
    return token

@pytest.fixture(scope="session")
def headers(token):
    return {
        'Authorization': f'OAuth {token}'
    }

@pytest.fixture
def temp_folder():
    """Генерирует уникальное имя папки"""
    return f"test-folder-{uuid4()}"

@pytest.fixture
def create_and_cleanup_folder(headers, temp_folder):
    """Создаёт папку и удаляет её после теста"""
    folder_path = f"disk:/{temp_folder}"
    # Создание
    response = requests.put(BASE_URL, headers=headers, params={'path': folder_path})
    assert response.status_code in [201, 409], f"Ошибка при создании: {response.text}"

    yield temp_folder  # передаём управление в тест

    # Удаление после теста
    requests.delete(BASE_URL, headers=headers, params={'path': folder_path, 'permanently': 'true'})
