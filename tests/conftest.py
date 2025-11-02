import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product


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
