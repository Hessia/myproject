# i create separate file for users so it wont look messy
import hashlib
def hash_password(password):
    """Hash a password for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, file_path="users.txt"):
    """Register a new user by saving their credentials."""
    with open(file_path, "a") as file:
        file.write(f"{username}, {hash_password(password)}\n")
        print("User registered succesfully!")

def login_user(username, password, file_path="users.txt"):
    """Check if the user exists and the password matches."""
    hashed_password = hash_password(password)
    try:
        with open(file_path, "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                stored_username = stored_username.strip()
                stored_password = stored_password.strip()
                if username == stored_username and hashed_password == stored_password:
                    print("Login succesful!")
                    return True
    except FileNotFoundError:
        print("User file not found.")
    print("Invalid password or username.")
    return False

