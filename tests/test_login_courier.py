import pytest
import requests
import allure

from data import BASE_URL, ENDPOINTS, STATUS_CODES
from generator import random_login, random_password

class TestsCourierLogin:

    @allure.title('Проверка успешной авторизации. POST /api/v1/courier/login')
    def test_courier_can_login(self, create_courier):
        _, login_courier_body, login, password = create_courier

        response = requests.post(f"{BASE_URL}{ENDPOINTS['COURIER_LOGIN']}", json=login_courier_body)

        assert response.status_code == STATUS_CODES['OK_SUCCESS']
        assert "id" in response.json() and isinstance(response.json()["id"], int)

    @allure.title('Проверка, что для авторизации нужно передать все обязательные поля. POST /api/v1/courier/login')
    @pytest.mark.parametrize('data_setup', [
        {"password": "test_password"},
        {"login": "test_login"},
    ])
    def test_login_missing_required_fields(self, data_setup):
        response = requests.post(f"{BASE_URL}{ENDPOINTS['COURIER_LOGIN']}", json=data_setup)

        assert response.status_code == STATUS_CODES['BAD_REQUEST']
        assert "message" in response.json()

    @allure.title('Проверка, что система возвращает ошибку при неверном логине. POST /api/v1/courier/login')
    def test_login_wrong_login(self, create_courier):
        _, login_courier_body, login, password = create_courier
        body = login_courier_body.copy()
        body["login"] = random_login()

        response = requests.post(f"{BASE_URL}{ENDPOINTS['COURIER_LOGIN']}", json=body)

        assert response.status_code == STATUS_CODES['NOT_FOUND']
        assert "message" in response.json()

    @allure.title('Проверка, что система возвращает ошибку при неверном пароле. POST /api/v1/courier/login')
    def test_login_wrong_password(self, create_courier):
        _, login_courier_body, login, password = create_courier
        body = login_courier_body.copy()
        body["password"] = random_password()

        response = requests.post(f"{BASE_URL}{ENDPOINTS['COURIER_LOGIN']}", json=body)

        assert response.status_code == STATUS_CODES['NOT_FOUND']
        assert "message" in response.json()

    @allure.title('Проверка, что система возвращает ошибку при авторизации под несуществующим пользователем. POST /api/v1/courier/login')
    def test_login_nonexistent_user(self):
        body = {
            "login": random_login(),
            "password": random_password()
        }

        response = requests.post(f"{BASE_URL}{ENDPOINTS['COURIER_LOGIN']}", json=body)

        assert response.status_code == STATUS_CODES['NOT_FOUND']
        assert "message" in response.json()
