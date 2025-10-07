import pytest
import requests
import allure

from data import BASE_URL, ENDPOINTS, STATUS_CODES
from generator import random_login, random_password, random_name

class TestsCreateCourier:

    @allure.title('Проверка успешного создания курьера. POST /api/v1/courier')
    def test_create_courier_success(self, generate_courier_data):
        create_body = generate_courier_data[0]

        response = requests.post(f"{BASE_URL}{ENDPOINTS['CREATE_COURIER']}", json=create_body)

        assert response.status_code == STATUS_CODES['CREATE_SUCCESS']
        assert response.json() == {"ok": True}

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров. POST /api/v1/courier')
    def test_create_duplicate_courier(self, create_courier):
        create_body = create_courier[0]

        response = requests.post(f"{BASE_URL}{ENDPOINTS['CREATE_COURIER']}", json=create_body)

        assert response.status_code == STATUS_CODES['CONFLICT']

    @allure.title('Проверка ошибки при отсутствии обязательных полей. POST /api/v1/courier')
    @pytest.mark.parametrize('data_setup', [
        {"password": random_password(), "firstName": random_name()},
        {"login": random_login(), "firstName": random_name()},
    ])
    def test_create_courier_missing_required_fields(self, data_setup):
        response = requests.post(f"{BASE_URL}{ENDPOINTS['CREATE_COURIER']}", json=data_setup)

        assert response.status_code == STATUS_CODES['BAD_REQUEST']