from src.product import Product


class LawnGrass(Product):
    """Класс для представления категории Трава газонная в интернет-магазине"""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return round(self.price * self.quantity + other.price * other.quantity, 2)
        raise TypeError
