import pytest
import uuid
from api_client import YougileAPI
from config import TEST_USER_ID


@pytest.fixture
def api_client():
    """Фикстура для создания клиента API"""
    return YougileAPI()


@pytest.fixture
def test_project_data():
    """Фикстура с тестовыми данными для проекта"""
    return {
        "title": f"Test Project {uuid.uuid4().hex[:6]}",
        "users": {
            TEST_USER_ID: "admin"
        }
    }


@pytest.fixture
def created_project(api_client, test_project_data):
    """Создает проект для тестов и возвращает его ID"""
    response = api_client.create_project(test_project_data)
    assert response.status_code == 201, (
        f"Failed to create test project: {response.text}")
    project_id = response.json().get("id")
    
    yield project_id
    
    # Очистка: удаляем созданный проект через PUT (устанавливаем deleted=true)
    try:
        api_client.update_project(project_id, {"deleted": True})
    except Exception:
        pass  # Игнорируем ошибки при очистке


@pytest.fixture
def test_user_id():
    """Фикстура с ID пользователя для тестов"""
    return TEST_USER_ID
