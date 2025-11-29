from src.order import Order
from src.product import Product


def test_order(product_test):
    order = Order(product_test, 2)
    assert order.name == "Заказ Тестовый товар"
    assert order.description == "Покупка товара Тестовый товар"
    assert order.total_price == 300


def test_order_str(product_test):
    order = Order(product_test, 2)
    assert str(order) == "Товар: Тестовый товар, Количество: 2, Стоимость: 300"


def test_custom_exception_order(capsys):

    new_product = Product.__new__(Product)
    new_product.name = "Тестовый товар"
    new_product.description = "Описание тестового товара"
    new_product._Product__price = 150
    new_product.quantity = 0

    Order(new_product, 0)
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[-2]
        == "Нельзя добавить товар с нулевым количеством"
    )
    assert (
        message.out.strip().split("\n")[-1]
        == "Обработка добавления товара в заказ завершена"
    )

    new_product = Product.__new__(Product)
    new_product.name = "Тестовый товар"
    new_product.description = "Описание тестового товара"
    new_product._Product__price = 150
    new_product.quantity = 3

    Order(new_product, 2)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар в заказ успешно добавлен"
    assert (
        message.out.strip().split("\n")[-1]
        == "Обработка добавления товара в заказ завершена"
    )
