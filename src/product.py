class Product:
    """Класс для товаров"""

    name: str
    description: str
    price: float
    quantity: int

    _products = [] # класс-аттрибут, в котором хранятся все экземпляры класса

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product._products.append(self)



    @classmethod
    def new_product(cls, new_product):
        for product in cls._products:
            if product.name == new_product.get("name"):
                product.quantity += int(new_product.get("quantity"))
                if product.__price < new_product.get("price"):
                    product.__price = new_product.get("price")
                return product
        else:
            return cls(new_product.get("name"), new_product.get("description"), new_product.get("price"),
                           new_product.get("quantity"))


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, actual_price):

        if actual_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if self.__price > actual_price:

            while True:

                confirmation = input("Цена товара понизится. Вы подтверждаете понижение цены? y/n").strip().lower()
                if confirmation.lower() == "y":
                    self.__price = actual_price
                    break

                elif confirmation.lower() == "n":
                    break
                else:
                    print("Введите y или n")
        else:
            self.__price = actual_price

