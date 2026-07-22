import uuid
from api_client import YougileAPI
from config import TEST_USER_ID


class TestProjects:
    """Тесты для методов работы с проектами Yougile"""

    # ==================== POST /api-v2/projects ====================

    def test_create_project_positive(self, api_client, test_user_id):
        """Позитивный тест создания проекта"""
        project_title = f"Test Project {uuid.uuid4().hex[:6]}"
        project_data = {
            "title": project_title,
            "users": {
                test_user_id: "admin"
            }
        }

        response = api_client.create_project(project_data)

        assert response.status_code == 201, (
            f"Expected 201, got {response.status_code}")
        response_data = response.json()
        assert "id" in response_data, "Response doesn't contain 'id' field"
        assert isinstance(
            response_data["id"], str), "Project ID should be a string"
        assert len(response_data["id"]) > 0, "Project ID should not be empty"

    def test_create_project_idempotent(self, api_client, test_user_id):
        """Позитивный тест создания проекта с идемпотентным ключом"""
        idempotency_key = uuid.uuid4().hex
        project_title = f"Test Project {uuid.uuid4().hex[:6]}"
        project_data = {
            "title": project_title,
            "users": {
                test_user_id: "admin"
            },
            "idempotencyKey": idempotency_key
        }

        response1 = api_client.create_project(project_data)
        assert response1.status_code == 201, (
            f"First request failed: {response1.status_code}")
        project_id1 = response1.json().get("id")

        response2 = api_client.create_project(project_data)
        assert response2.status_code == 201, (
            f"Second request failed: {response2.status_code}")
        project_id2 = response2.json().get("id")

        msg = "Idempotency key didn't work properly"
        assert project_id1 == project_id2, msg

    def test_create_project_no_title(self, api_client, test_user_id):
        """Негативный тест: создание проекта без обязательного поля title"""
        project_data = {
            "users": {
                test_user_id: "admin"
            }
        }

        response = api_client.create_project(project_data)

        assert response.status_code == 400, (
            f"Expected 400, got {response.status_code}")
        response_data = response.json()
        has_error = "error" in response_data
        has_message = "message" in response_data
        has_title = "title" in str(response_data)
        assert has_error or has_message or has_title, (
            "Response should contain error message about missing title")

    def test_create_project_empty_title(self, api_client, test_user_id):
        """Негативный тест: создание проекта с пустым названием"""
        project_data = {
            "title": "",
            "users": {
                test_user_id: "admin"
            }
        }

        response = api_client.create_project(project_data)

        assert response.status_code in [400, 422], \
            f"Expected 400 or 422, got {response.status_code}"
        response_data = response.json()
        assert "error" in response_data or "message" in response_data, \
            "Response should contain error message"

    def test_create_project_invalid_role(self, api_client, test_user_id):
        """Негативный тест: создание проекта с несуществующей ролью"""
        project_data = {
            "title": f"Test Project {uuid.uuid4().hex[:6]}",
            "users": {
                test_user_id: "invalid_role_123"
            }
        }

        response = api_client.create_project(project_data)

        assert response.status_code in [400, 422], \
            f"Expected 400 or 422, got {response.status_code}"

    def test_create_project_unauth(self):
        """Негативный тест: создание проекта без авторизации"""
        api = YougileAPI(token="invalid_token")

        project_data = {
            "title": "Test Project",
            "users": {
                TEST_USER_ID: "admin"
            }
        }

        response = api.create_project(project_data)

        assert response.status_code == 401, (
            f"Expected 401, got {response.status_code}")

    # ==================== GET /api-v2/projects/{id} ====================

    def test_get_project_positive(self, api_client, created_project):
        """Позитивный тест получения проекта по ID"""
        response = api_client.get_project(created_project)

        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}")
        response_data = response.json()

        msg = "Project ID doesn't match"
        assert response_data.get("id") == created_project, msg
        msg = "Response doesn't contain 'title' field"
        assert "title" in response_data, msg
        msg = "Response doesn't contain 'timestamp' field"
        assert "timestamp" in response_data, msg
        msg = "Response doesn't contain 'users' field"
        assert "users" in response_data, msg
        assert isinstance(response_data.get("timestamp"), (int, float)), (
            "Timestamp should be a number")
        # assert response_data.get(
        #     "deleted") is not None, "Response should contain 'deleted' field"

    def test_get_project_verify_data(
            self,
            api_client,
            test_project_data,
            created_project):
        """Позитивный тест: проверка соответствия данных при получении"""
        response = api_client.get_project(created_project)

        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}")
        response_data = response.json()

        assert response_data.get("title") == test_project_data["title"], \
            "Project title doesn't match"
        # assert response_data.get("deleted") is False, \
        #     "Newly created project should have deleted=false"

    def test_get_project_not_found(self, api_client):
        """Негативный тест: получение несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api_client.get_project(fake_id)

        assert response.status_code == 404, (
            f"Expected 404, got {response.status_code}")
        response_data = response.json()
        assert "error" in response_data or "message" in response_data, \
            "Response should contain error message"

    def test_get_project_invalid_id(self, api_client):
        """Негативный тест: получение проекта с некорректным форматом ID"""
        invalid_id = "invalid-id-format"
        response = api_client.get_project(invalid_id)

        assert response.status_code in [400, 404], \
            f"Expected 400 or 404, got {response.status_code}"

    def test_get_project_unauth(self, api_client, created_project):
        """Негативный тест: получение проекта с невалидным токеном"""
        api = YougileAPI(token="invalid_token")

        response = api.get_project(created_project)

        assert response.status_code == 401, (
            f"Expected 401, got {response.status_code}")

    # ==================== PUT /api-v2/projects/{id} ====================

    def test_update_project_title(self, api_client, created_project):
        """Позитивный тест обновления названия проекта"""
        new_title = f"Updated Project {uuid.uuid4().hex[:6]}"
        update_data = {
            "title": new_title
        }

        response = api_client.update_project(created_project, update_data)

        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}")
        response_data = response.json()
        assert response_data.get(
            "id") == created_project, "Project ID doesn't match"

        get_response = api_client.get_project(created_project)
        assert get_response.status_code == 200, "Failed to get updated project"
        msg = "Project ID doesn't match"
        assert response_data.get("id") == created_project, msg

    def test_update_project_users(
            self,
            api_client,
            created_project,
            test_user_id):
        """Позитивный тест обновления пользователей проекта"""
        update_data = {
            "users": {
                test_user_id: "observer"
            }
        }

        response = api_client.update_project(created_project, update_data)

        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}")
        response_data = response.json()
        assert response_data.get(
            "id") == created_project, "Project ID doesn't match"

    def test_update_project_deleted(self, api_client, created_project):
        """Позитивный тест: мягкое удаление проекта"""
        update_data = {
            "deleted": True
        }

        response = api_client.update_project(created_project, update_data)

        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}")

        get_response = api_client.get_project(created_project)
        assert get_response.status_code == 200, "Failed to get updated project"
        assert get_response.json().get(
            "deleted") is True, "Project should be marked as deleted"

    def test_update_project_not_found(self, api_client):
        """Негативный тест: обновление несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        update_data = {
            "title": "Updated Name"
        }

        response = api_client.update_project(fake_id, update_data)

        assert response.status_code == 404, (
            f"Expected 404, got {response.status_code}")
        response_data = response.json()
        assert "error" in response_data or "message" in response_data, \
            "Response should contain error message"

    def test_update_project_empty_title(self, api_client, created_project):
        """Негативный тест: обновление проекта с пустым названием"""
        update_data = {
            "title": ""
        }

        response = api_client.update_project(created_project, update_data)

        assert response.status_code in [400, 422], \
            f"Expected 400 or 422, got {response.status_code}"

    def test_update_project_invalid_role(
            self, api_client, created_project, test_user_id):
        """Негативный тест: обновление проекта с несуществующей ролью"""
        update_data = {
            "users": {
                test_user_id: "invalid_role"
            }
        }

        response = api_client.update_project(created_project, update_data)

        assert response.status_code in [400, 422], \
            f"Expected 400 or 422, got {response.status_code}"

    def test_update_project_unauth(self, api_client, created_project):
        """Негативный тест: обновление проекта с невалидным токеном"""
        api = YougileAPI(token="invalid_token")
        update_data = {
            "title": "Unauthorized Update"
        }

        response = api.update_project(created_project, update_data)

        assert response.status_code == 401, (
            f"Expected 401, got {response.status_code}")

    def test_update_project_invalid_id(self, api_client):
        """Негативный тест: обновление с некорректным форматом ID"""
        invalid_id = "invalid-id-format"
        update_data = {
            "title": "Updated Name"
        }

        response = api_client.update_project(invalid_id, update_data)

        assert response.status_code in [400, 404], \
            f"Expected 400 or 404, got {response.status_code}"

    def test_update_project_no_fields(self, api_client, created_project):
        """Негативный тест: обновление без указания полей"""
        update_data = {}

        response = api_client.update_project(created_project, update_data)

        assert response.status_code in [200, 400], \
            f"Expected 200 or 400, got {response.status_code}"
