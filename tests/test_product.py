from src.product import Product


def test_product_init(product_5):
    assert product_5.name == "Product_5"
    assert product_5.description == "description of Product_5"
    assert product_5.price == 25.94
    assert product_5.quantity == 3

def test_new_product():
    product = {"name": "Новый товар", "description": "Описание нового товара", "price": 56.78, "quantity": 4}
    New_product = Product.new_product(product)
    assert New_product.name == "Новый товар"
    assert New_product.description == "Описание нового товара"
    assert New_product.price == 56.78
    assert New_product.quantity == 4

def test_new_product_same_name():
    product_1 = Product("Товар_1", "Описание товара_1", 10.90, 4)
    product_2 = {"name": "Товар_1", "description": "Описание товара_1", "price": 11.90, "quantity": 2}
    Product.new_product(product_2)

    assert product_1.quantity == 6
    assert product_1.price == 11.90