from ..key import set_secret_value

def set_secret(secret_name, secret_value):
    result = set_secret_value(secret_name, secret_value)
    print(f"Se actualizó el secreto '{secret_name}'")
    return result

if __name__ == "__main__":
    set_secret("LuisAWS", "Proyecto DevRootDark Estructura Limpia")