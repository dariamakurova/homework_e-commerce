import json
import os

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


if __name__ == "__main__":

    path = os.path.join(
        (os.path.dirname(os.path.dirname(__file__))), "data", "products.json"
    )
    data_ = open_json(path)
    categories_ = create_objects_from_json(data_)
    print(categories_)

    print(categories_[0].name)
    print(categories_[0].description)
