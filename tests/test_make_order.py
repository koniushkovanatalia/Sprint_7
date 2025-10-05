import pytest
import requests
import allure

from data import BASE_URL, ENDPOINTS, STATUS_CODES, DataForOrder

class TestCreateOrder:

    @allure.title('Проверка, что можно оформить заказ с одним из цветов BLACK или GREY. POST /api/v1/orders')
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"]])
    def test_create_order_single_color(self, color):
        order_data = DataForOrder.order_data.copy()
        order_data["color"] = color

        response = requests.post(f"{BASE_URL}{ENDPOINTS['CREATE_ORDER']}", json=order_data)
        assert response.status_code == STATUS_CODES["CREATE_SUCCESS"]
        response_json = response.json()
        assert "track" in response_json
        assert isinstance(response_json["track"], int)

    @allure.title('Проверка, что можно выбрать оба цвета. POST /api/v1/orders')
    def test_create_order_black_grey(self):
        order_data = DataForOrder.order_data.copy()
        order_data["color"] = ["BLACK", "GREY"]

        response = requests.post(f"{BASE_URL}{ENDPOINTS['CREATE_ORDER']}", json=order_data)
        assert response.status_code == STATUS_CODES["CREATE_SUCCESS"]
        response_json = response.json()
        assert "track" in response_json
        assert isinstance(response_json["track"], int)

    @allure.title('Проверка, что цвет можно не указывать. POST /api/v1/orders')
    def test_create_order_no_color(self):
        order_data = DataForOrder.order_data.copy()
        order_data["color"] = []

        response = requests.post(f"{BASE_URL}{ENDPOINTS['CREATE_ORDER']}", json=order_data)
        assert response.status_code == STATUS_CODES["CREATE_SUCCESS"]
        response_json = response.json()
        assert "track" in response_json
        assert isinstance(response_json["track"], int)