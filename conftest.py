import pytest
import requests
from data import BASE_URL, ENDPOINTS
from generator import random_login, random_password, random_name

@pytest.fixture
def create_courier():
    # генерируем данные курьера
    login = random_login()
    password = random_password()
    first_name = random_name()

    create_courier_body = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    login_courier_body = {
        "login": login,
        "password": password
    }

    # создаем курьера
    requests.post(f"{BASE_URL}{ENDPOINTS['CREATE_COURIER']}", json=create_courier_body)

    # логин курьера в системе
    login_courier = requests.post(f"{BASE_URL}{ENDPOINTS['COURIER_LOGIN']}", json=login_courier_body)

    yield [create_courier_body, login_courier_body, login, password]

    # удаляем курьера
    courier_id = login_courier.json().get("id")
    requests.delete(f"{BASE_URL}{ENDPOINTS['COURIER_DELETE'].replace(':id', str(courier_id))}")

@pytest.fixture
def generate_courier_data():
    # генерация данных
    login = random_login()
    password = random_password()
    first_name = random_name()

    create_courier_body = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    login_courier_body = {
        "login": login,
        "password": password
    }

    # логин курьера в системе
    login_courier = requests.post(f"{BASE_URL}{ENDPOINTS['COURIER_LOGIN']}", json=login_courier_body)

    yield [create_courier_body, login_courier_body]

    # удаляем курьера
    courier_id = login_courier.json().get("id")
    requests.delete(f"{BASE_URL}{ENDPOINTS['COURIER_DELETE'].replace(':id', str(courier_id))}")




