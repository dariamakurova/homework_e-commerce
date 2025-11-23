import pytest


def test_category_iterator(category_iterator):
    assert category_iterator.index == 0
    assert next(category_iterator) == "Product_1, 25.94 руб. Остаток: 3 шт.\n"
    assert next(category_iterator) == "Product_2, 33.55 руб. Остаток: 6 шт.\n"
    with pytest.raises(StopIteration):
        next(category_iterator)
