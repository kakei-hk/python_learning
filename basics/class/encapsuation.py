class ProductAccessorMethod:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    # getter for id
    def get_id(self):
        return self.__id

    # getter for name
    def get_name(self):
        return self.__name

    # getter for price
    def get_price(self):
        return self.__price

    # setter for name
    def set_name(self, name_new):
        self.__name = name_new

    # setter for price
    def set_price(self, price_new):
        if price_new < 0:
            raise ValueError("price must be positive value!")
        self.__price = price_new

    def show_info(self):
        print(f"id: {self.get_id()}")
        print(f"name: {self.get_name()}")
        print(f"price: {self.get_price()} yen")


class ProductProperty:
    def __init__(self, id, name, price):
        self.__id = id
        self.name = name
        self.price = price

    # getters
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    # setters
    @name.setter
    def name(self, name_new):
        self.__name = name_new

    @price.setter
    def price(self, price_new):
        if price_new < 0:
            raise ValueError("price must be positive value!")
        self.__price = price_new

    def show_info(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"price: {self.price} yen")


if __name__ == "__main__":
    product_a = ProductAccessorMethod(1, "python_book", 2000)
    product_a.show_info()
    print()

    product_a.set_price(3000)
    # price cannot be set directly
    product_a.__price = 2500
    product_a.show_info()
    print()

    product_b = ProductProperty(2, "c_book", 1000)
    product_b.show_info()
    print()

    product_b.price = 1500
    # error occurs, not an assignment to an instance variable but actually a getter
    # product_b.price = -100
    product_b.show_info()
