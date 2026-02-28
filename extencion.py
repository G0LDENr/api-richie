from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

Swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API",
        "description": "Api del 83",
        "version": "2.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Aqui va a barrer el <token>"
        }
    } 
}

# Inicializa Swagger correctamente
swagger = Swagger(template=Swagger_template)