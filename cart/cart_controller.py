from .cart_model import CartItemFactory

def add_to_cart(cart, product, quantity):
    cart_item = CartItemFactory.create_cart_item(product, quantity)
    cart.append(cart_item)
    print(f"Added {quantity} of {product.name} to cart.")
