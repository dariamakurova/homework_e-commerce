from src.product import Product


def test_product_init(product_1):
    assert product_1.name == "Product_1"
    assert product_1.description == "description of Product_1"
    assert product_1.price == 25.94
    assert product_1.quantity == 3
