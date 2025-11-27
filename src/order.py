from src.base_category import BaseCategory
from src.exceptions import ZeroQuantity
from src.product import Product


class Order(BaseCategory):
    """Класс для создания заказов"""

    product: Product
    quantity: int

    def __init__(self, product, quantity):
        super().__init__(
            name=f"Заказ {product.name}", description=f"Покупка товара {product.name}"
        )
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantity("Нельзя добавить товар с нулевым количеством")
            except ZeroQuantity as e:
                print(str(e))
            else:
                self.product = product
                self.quantity = quantity
                self.total_price = self.product.price * quantity
                print("Товар в заказ успешно добавлен")
            finally:
                print("Обработка добавления товара в заказ завершена")

    def __str__(self):
        return f"Товар: {self.product.name}, Количество: {self.quantity}, Стоимость: {self.total_price}"
