class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class CartItemFactory:
    @staticmethod
    def create_cart_item(product, quantity):
        return CartItem(product, quantity)
