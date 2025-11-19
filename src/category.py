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

    def __str__(self):
        amount = 0
        for product in self.__products:
            amount += product.quantity
        return f"{self.name}, количество продуктов: {amount} шт."

    @property
    def products(self):
        """Возвращает список товаров в виде строк с информацией о товаре"""
        product_str = [f"{str(product)}\n" for product in self.__products]
        return product_str

    def add_product(self, product):
        """Добавление товара в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def get_products(self):
        """Получение списка товаров"""
        return self.__products
