from src.product import Product


class LawnGrass(Product):
    def __init__(self, name, description, price, country, germination_period, color):
        super().__init__(name, description, price)
        self.country = country
        self.germination_period = germination_period
        self.color = color
