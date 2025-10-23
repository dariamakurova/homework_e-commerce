
class Category:
    """ Класс для категорий товаров """

    name: str
    description: str
    products: list

    number_of_categories = 0
    number_of_products = 0


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.number_of_categories += 1
        Category.number_of_products += len(self.products)

