from .order_model import Order

def place_order(user, cart):
    order = Order(user, cart)
    print(f"Order placed by {user.username} for {len(cart)} items.")
