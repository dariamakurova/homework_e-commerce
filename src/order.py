from src.base_category import BaseCategory
from src.product import Product


class Order(BaseCategory):
    """ Класс для создания заказов """

    product: Product
    quantity: int

    def __init__(self, product, quantity):
        super().__init__(name=f"Заказ {product.name}", description=f"Покупка товара {product.name}")
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * quantity

    def __str__(self):
        return(f"Товар: {self.product.name}, Количество: {self.quantity}, Стоимость: {self.total_price}")


if __name__ == "__main__":

    product_1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    order_1 = Order("Sony", 10, 125000)
    order_1.add_product(product_1, 2)