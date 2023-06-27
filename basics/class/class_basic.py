class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def show_info(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"price: {self.price} yen")


if __name__ == "__main__":
    product_a = Product(1, "python_book", "2000")
    product_a.show_info()
