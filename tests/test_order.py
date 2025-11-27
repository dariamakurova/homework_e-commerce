from src.order import Order


def test_order(product_test):
    order = Order(product_test, 2)
    assert order.name == "Заказ Тестовый товар"
    assert order.description == "Покупка товара Тестовый товар"
    assert order.total_price == 300


def test_order_str(product_test):
    order = Order(product_test, 2)
    assert str(order) == "Товар: Тестовый товар, Количество: 2, Стоимость: 300"
