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