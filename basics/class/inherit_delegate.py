# base class
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def show_info(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"price: {self.price} yen")


class TestMultiply:
    def __init__(self, num_a, num_b):
        self.num_a = num_a
        self.num_b = num_b

    def multiply(self):
        return self.num_a * self.num_b


# class inheritance
class Food(Product):
    def __init__(self, id, name, calorie, price):
        super().__init__(id, name, price)
        # add calorie
        self.calorie = calorie

    def show_info(self):
        # override show_info method of base class
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"calorie: {self.calorie} kcal")
        print(f"price: {self.price} yen")


# class delegation
class ProductMulti:
    def __init__(self, id, name, price, num):
        self.id = id
        self.name = name
        self.price = price
        self.num = num
        # for delegation
        self.__multiply = TestMultiply(price, num)

    def show_info(self):
        total_price = self.__multiply.multiply()
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"price: {self.price} yen")
        print(f"number: {self.num}")
        print(f"total price: {total_price} yen")


if __name__ == "__main__":
    product_a = Product(1, "python_book", 2000)
    product_a.show_info()
    print()

    product_b = Food(2, "curry_rice", 900, 1000)
    product_b.show_info()
    print()

    product_c = ProductMulti(3, "pencil", 100, 16)
    product_c.show_info()
