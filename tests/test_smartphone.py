import pytest


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == "Nokia"
    assert smartphone_1.description == "Кнопочный телефон"
    assert smartphone_1.price == 100
    assert smartphone_1.quantity == 2
    assert smartphone_1.model == "3310"
    assert smartphone_1.efficiency == 3
    assert smartphone_1.memory == 10
    assert smartphone_1.color == "синий"

def test_smartphone_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 560

def test_smartphone_add_error(smartphone_1, smartphone_2):
    with pytest.raises(TypeError):
        result = smartphone_1 + 3

