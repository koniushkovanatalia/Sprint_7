from datetime import datetime, timedelta

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

ENDPOINTS = {
    "CREATE_COURIER": "/courier", # создание курьера
    "COURIER_LOGIN": "/courier/login", # логин курьера в системе
    "COURIER_DELETE": "/courier/:id", # удаление курьера
    "CREATE_ORDER": "/orders", # создание заказа
    "GET_ORDER": "/orders/track", # получить заказ по его номеру
    "GET_ORDER_LIST": "/orders" # получить список заказов
}

STATUS_CODES = {
    "OK_SUCCESS": 200,
    "CREATE_SUCCESS": 201,
    "BAD_REQUEST": 400,
    "NOT_FOUND": 404,
    "CONFLICT": 409
}

class DataForOrder:
    order_data = {
    "firstName": "Tony",
    "lastName": "Stark",
    "address": "Stark Tower, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 000 00 01",
    "rentTime": 5,
    "deliveryDate": (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'),
    "comment": "We have a Hulk"
    }

    scooter_color = [['BLACK'], ['GREY'], ['BLACK', 'GREY'], ['']]


