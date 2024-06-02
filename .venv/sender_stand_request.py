# Бутычин Станислав, 16-я когорта - финальный проект, инженер по тестированию плюс

import configuration
import requests
import data


def create_order(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDER, json=body)

def get_order(track_number):
    get_order_url=f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    responce = requests.get(get_order_url)
    return responce


def test_order_creation_and_retrieval_test():
    responce = create_order(data.order_body)
    track_number=responce.json()["track"]
    print("Заказ создан, трек-номер:", track_number)

    order_responce = get_order(track_number)
    assert order_responce.status_code==200, f"Ошибка: {order_responce.status_code}"
    order_data=order_responce.json()
    print("Данные заказа:")
    print(order_data)