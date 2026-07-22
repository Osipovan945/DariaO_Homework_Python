import requests
from config import BASE_URL, AUTH_TOKEN


class YougileAPI:
    """Клиент для работы с API Yougile"""
    
    def __init__(self, token=None):
        self.base_url = BASE_URL
        self.token = token or AUTH_TOKEN
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def create_project(self, data):
        """Создание проекта"""
        url = f"{self.base_url}/projects"
        response = requests.post(url, json=data, headers=self.headers)
        return response
    
    def get_project(self, project_id):
        """Получение проекта по ID"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response
    
    def update_project(self, project_id, data):
        """Обновление проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.put(url, json=data, headers=self.headers)
        return response
    