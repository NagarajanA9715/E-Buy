from .user_model import User

def register_user():
    name = input("Enter username: ")
    email = input("Enter email: ")
    user = User(name, email)
    print(f"User {user.username} registered.")
