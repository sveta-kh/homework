#Shopping Cart

class ShoppingCart:
    def __init__(self,) -> None:
        self.cart: list = []
    def add_product(self):
        product = input("Enter product: ")
        self.cart.append(product)

    def remove_product(self):
        product = input("Remove product: ")
        self.cart.pop()

cart1 = ShoppingCart()
cart1.add_product()
cart1.add_product()
cart1.add_product()
cart1.add_product()
print(cart1.cart)

cart1.remove_product()
print(cart1.cart)




