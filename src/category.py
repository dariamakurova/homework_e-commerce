from itertools import product


class Category:
    """Класс для категорий товаров"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)


    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f'{product.name}, {product.price}. Остаток: {product.quantity} шт.\n'
        return product_str


    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

