import json


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    @classmethod
    def init_with_json(cls, json_path):  # factory method
        with open(json_path) as f:
            product_info = json.load(f)
        return cls(product_info["id"], product_info["name"], product_info["price"])

    @staticmethod
    def explain_class():
        print("This class is prepared for testing!")

    def show_info(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"price: {self.price} yen")


if __name__ == "__main__":
    product_info_path = "product_info.json"
    book = Product.init_with_json(product_info_path)
    book.show_info()
    Product.explain_class()
