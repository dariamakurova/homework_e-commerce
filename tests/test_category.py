from src.category import Category


def test_category_init(category_1, category_2):
    assert category_1.name == "Category_1"
    assert category_1.description == "Category_of_products_1"
    assert category_1.products == ["product_1", "product_2"]

    assert category_2.name == "Category_2"
    assert category_2.description == "Category_of_products_2"
    assert category_2.products == ["product_3", "product_4"]

    assert Category.number_of_categories == 2
    assert Category.number_of_products == 4
