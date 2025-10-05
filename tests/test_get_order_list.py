import pytest
import requests
import allure

from data import BASE_URL, ENDPOINTS, STATUS_CODES


class TestGetOrders:

    @allure.title('Проверка, что можно получить список заказов. GET /api/v1/orders')
    def test_get_orders_list(self):
        response = requests.get(f"{BASE_URL}{ENDPOINTS['GET_ORDER_LIST']}")
        assert response.status_code == STATUS_CODES["OK_SUCCESS"]

        response_json = response.json()
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)
