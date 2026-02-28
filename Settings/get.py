from ..key import get_secret_value

def get_secret(secret_name):
    secret = get_secret_value(secret_name)
    print(f"El secreto '{secret_name}' es: {secret}")
    return secret

if __name__ == "__main__":
    get_secret("LuisAWS")