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
        """ Возвращает список товаров в виде строки """
        product_str = ""
        for product in self.__products:
            product_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_str


    def add_product(self, product):
        """ Добавление товара в категорию """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def get_products(self):
        """ Получение списка товаров"""
        return self.__products