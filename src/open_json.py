import json
import os


def open_json(file):
    """ Получение данных из json файла и создание объектов класса """


    products = json.load(file)



if __name__ == "__main__":

    path = os.path.join((os.path.dirname(os.path.dirname(__file__))), "data", "products.json")