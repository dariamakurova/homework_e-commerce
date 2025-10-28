from src.category import Category
from tests.conftest import category_1


def test_category_init(category_1, category_2):
    assert category_1.name == "Category_1"
    assert category_1.description == "Category_of_products_1"
    assert len(category_2.get_products) == 2

    assert category_2.name == "Category_2"
    assert category_2.description == "Category_of_products_2"
    assert category_2.get_products == ["product_3", "product_4"]

    assert Category.category_count == 2
    assert Category.product_count == 4

def test_products_property(category_1):
    assert category_1.products == ("Product_1, 25.94 руб. Остаток: 3 шт.\nProduct_2, 33.55 руб. Остаток: 6 шт.\n")

def test_add_product(category_1, product_5):
    assert len(category_1.get_products) == 2
    category_1.add_product(product_5)
    assert len(category_1.get_products) == 3

