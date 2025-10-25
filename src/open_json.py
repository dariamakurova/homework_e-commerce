import json

from src.category import Category
from src.product import Product


def open_json(path):
    """Получение данных из json файла и создание объектов класса"""

    with open(path, "r", encoding="UTF-8") as file:
        products = json.load(file)
    return products


def create_objects_from_json(data):

    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
