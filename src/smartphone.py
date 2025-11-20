from src.product import Product


class Smartphone(Product):
    """ Класс для представления товара Смартфоны в интернет-магазине """

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    def __add__(self, other):
        if type(other) is Smartphone:
            return round(self.price * self.quantity + other.price * other.quantity, 2)
        raise TypeError
