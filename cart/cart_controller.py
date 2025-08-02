from .cart_model import CartItem

def add_to_cart(cart, product, quantity):
    cart.append(CartItem(product, quantity))
    print(f"Added {quantity} of {product.name} to cart.")
