from flask import Flask
from Controllers.HomeController import Blueprint_home
from extencion import db, migrate, swagger, jwt
from config import Config
from Controllers.AuthController import auth_bp
from Controllers.UserController import user_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app) 
    jwt.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)
    
    app.register_blueprint(auth_bp,url_prefix='/api/auth')
    app.register_blueprint(user_db,url_prefix='/api/me')
    
    app.register_blueprint(Blueprint_home)
    @app.route('/')
    def home():
        return {'mensaje': 'hola mundo hhhh'}, 400   

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8000)