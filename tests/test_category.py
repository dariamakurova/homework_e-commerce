import pytest

from src.category import Category


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
    assert category_1.products == (
        [
            "Product_1, 25.94 руб. Остаток: 3 шт.\n",
            "Product_2, 33.55 руб. Остаток: 6 шт.\n",
        ]
    )


def test_add_product(category_1, product_5):
    assert len(category_1.get_products) == 2
    category_1.add_product(product_5)
    assert len(category_1.get_products) == 3


def test_category_str(category_1):
    assert str(category_1) == "Category_1, количество продуктов: 9 шт."


def test_add_product_not_product(category_2):
    with pytest.raises(TypeError):
        category_2.add_product("not_product")


def test_add_product_smartphone(category_2, smartphone_1):
    category_2.add_product(smartphone_1)
    assert category_2.get_products[-1].name == "Nokia"
