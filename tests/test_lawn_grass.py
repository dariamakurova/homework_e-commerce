import pytest


def test_lawn_grass_init(lawn_grass_1):
    assert lawn_grass_1.name == "Газонная трава 1"
    assert lawn_grass_1.description == "Смесь клевер, мятлик"
    assert lawn_grass_1.price == 1500
    assert lawn_grass_1.quantity == 4
    assert lawn_grass_1.country == "Россия"
    assert lawn_grass_1.germination_period == "7 дней"
    assert lawn_grass_1.color == "сочный зеленый"


def test_lawn_grass_add(lawn_grass_1, lawn_grass_2):
    assert lawn_grass_1 + lawn_grass_2 == 12000


def test_lawn_grass_add_error(lawn_grass_1, lawn_grass_2):
    with pytest.raises(TypeError):
        lawn_grass_2() + 3
