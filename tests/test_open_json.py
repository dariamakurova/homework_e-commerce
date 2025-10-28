from unittest.mock import patch

from src.category import Category
from src.open_json import create_objects_from_json, open_json


@patch("json.load")
def test_open_json(mock_read):
    mock_read.return_value = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций "
            "для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
            ],
        }
    ]
    assert open_json(mock_read) == [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций "
            "для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
            ],
        }
    ]


def test_create_objects_from_json(json_data):
    result = create_objects_from_json(json_data)
    category = result[0]
    assert isinstance(category, Category)

    assert category.name == "Смартфоны"
    assert category.description.strip() == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получение дополнительных функций для удобства жизни"
    )
