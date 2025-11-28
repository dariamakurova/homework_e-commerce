from src.base_category import BaseCategory
from src.product import Product
from src.exceptions import ZeroQuantity


class Category(BaseCategory):
    """Класс для категорий товаров"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        super().__init__(name, description)
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
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantity("Нельзя добавить товар с нулевым количеством")
            except ZeroQuantity as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар успешно добавлен")
            finally:
                print("Обработка добавления товара в категорию завершена")
        else:
            raise TypeError

    @property
    def get_products(self):
        """Получение списка товаров"""
        return self.__products

    def middle_price(self):
        try:
            return round(
                sum([product.price for product in self.__products])
                / len(self.__products),
                2,
            )
        except ZeroDivisionError:
            return 0
