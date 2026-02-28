from flask import Blueprint

Blueprint_home = Blueprint('home', __name__)
@Blueprint_home.route('/home')
def home():
    return {"mensaje": "Hola desde home"}