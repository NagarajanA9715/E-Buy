from .product_model import Product

def list_products():
    products = [
        Product(1, "Laptop", 75000),
        Product(2, "Smartphone", 25000)
    ]
    for product in products:
        print(f"{product.id}: {product.name} - ₹{product.price}")
