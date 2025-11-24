from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):

    Product("Тестовый товар", "Описание тестового продукта", 150, 6)
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "Product('Тестовый товар', 'Описание тестового продукта', 150, 6)"
    )

    Smartphone("Nokia", "Кнопочный телефон", 100, 2, 3, "3310", 10, "синий")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone('Nokia', 'Кнопочный телефон', 100, 2)"

    LawnGrass(
        "Газонная трава 1",
        "Смесь клевер, мятлик",
        1500,
        4,
        "Россия",
        "7 дней",
        "сочный зеленый",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "LawnGrass('Газонная трава 1', 'Смесь клевер, мятлик', 1500, 4)"
    )
