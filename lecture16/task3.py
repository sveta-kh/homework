#Online Store Product

class Product:
    shop_name = "MegaShop"

    def __init__(self, name, price, stock) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
      self.stock -= quantity

      print(f"Sold: {quantity} laptops, remaining: {self.stock}")


sell1 = Product("Macbook", "2000.0$", 20)
sell1.sell(5)



   