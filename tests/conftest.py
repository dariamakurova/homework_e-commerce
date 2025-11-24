import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def category_1():

    product_1 = Product(
        name="Product_1",
        description="description of Product_1",
        price=25.94,
        quantity=3,
    )
    product_2 = Product(
        name="Product_2",
        description="description of Product_2",
        price=33.55,
        quantity=6,
    )

    return Category(
        name="Category_1",
        description="Category_of_products_1",
        products=[product_1, product_2],
    )


@pytest.fixture
def category_2():
    return Category(
        name="Category_2",
        description="Category_of_products_2",
        products=["product_3", "product_4"],
    )


@pytest.fixture
def product_5():
    return Product(
        name="Product_5",
        description="description of Product_5",
        price=25.94,
        quantity=3,
    )


@pytest.fixture
def product_6():
    return Product(
        name="Product_6",
        description="description of Product_6",
        price=13.44,
        quantity=12,
    )


@pytest.fixture
def json_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций "
            "для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
            ],
        }
    ]


@pytest.fixture
def category_iterator(category_1):
    return CategoryIterator(category_1)


@pytest.fixture
def smartphone_1():
    return Smartphone("Nokia", "Кнопочный телефон", 100, 2, 3, "3310", 10, "синий")


@pytest.fixture
def smartphone_2():
    return Smartphone(
        "SonyEriksson",
        "Телефон со стилусом",
        120,
        3,
        5,
        "Walkman 5800",
        36,
        "оранжевый",
    )


@pytest.fixture
def lawn_grass_1():
    return LawnGrass(
        "Газонная трава 1",
        "Смесь клевер, мятлик",
        1500,
        4,
        "Россия",
        "7 дней",
        "сочный зеленый",
    )


@pytest.fixture
def lawn_grass_2():
    return LawnGrass(
        "Газонная трава 2",
        "Элитный газон",
        2000,
        3,
        "Нидерланды",
        "5 дней",
        "темно-зеленый",
    )

@pytest.fixture
def product_test():
    return Product(
        "Тестовый товар",
        "Описание тестового продукта",
        150,
        6)