from users.user_controller import register_user
from products.product_controller import list_products

def main():
    print("Welcome to E-Buy!")
    register_user()
    list_products()

if __name__ == "__main__":
    main()
