class Product:
    """Класс для товаров"""

    name: str
    description: str
    price: float
    quantity: int

    _products = [] # класс-аттрибут, в котором хранятся все экземпляры класса

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product._products.append(self)



    @classmethod
    def new_product(cls, new_product):
        for product in cls._products:
            if product.name == new_product.get("name"):
                product.quantity += int(new_product.get("quantity"))
                if product.price < new_product.get("price"):
                    product.price = new_product.get("price")
                return product
        else:
            return cls(new_product.get("name"), new_product.get("description"), new_product.get("price"),
                           new_product.get("quantity"))


