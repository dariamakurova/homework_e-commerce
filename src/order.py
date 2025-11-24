from src.base_category import BaseCategory
from src.product import Product


class Order(BaseCategory):
    """Класс для создания заказов"""

    product: Product
    quantity: int

    def __init__(self, product, quantity):
        super().__init__(
            name=f"Заказ {product.name}", description=f"Покупка товара {product.name}"
        )
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * quantity

    def __str__(self):
        return f"Товар: {self.product.name}, Количество: {self.quantity}, Стоимость: {self.total_price}"
