class Product:
    """Класс для товаров"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product):
        return cls(product.get("name"), product.get("description"), product.get("price"), product.get("quantity"))