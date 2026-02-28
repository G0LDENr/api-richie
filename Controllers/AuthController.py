from Services.AuthServices import authService
from flask import Blueprint,request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register', methods=['POST'])
@swag_from({
    'tags': ['User'],
    "security": [{"BearerAuth": []}],
    'parameters': [
        {'name': 'body', 
        'in': 'body',
        'schema': {
            'type': 'object',
            'properties': {
                'username': {'type': 'string'},
                'email': {'type': 'string'},
                'password': {'type': 'string'}
            },
            'required': ['username', 'email', 'password']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Usuario creado',
        }
    }
})
def register():
    data = request.get_json()
    try:
        user = authService.register(data['username'], data['email'], data['password'])
        print('USER', user)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        print(e)
        return jsonify({'message': str(e)}), 500

@auth_bp.route('/user/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['User'],
    "security": [{"BearerAuth": []}],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Información del usuario',
            "examples": {
                "application/json": {
                    "id": 2,
                    "username": "usuario_ejemplo",
                    "email": "usuario_ejemplo@example.com"
                }
            }
        },
        404: {
            'description': 'Usuario no encontrado',
        }
    }
})
def get_user(id):
    try:
        user = authService.find_by_id(id)
        if user:
            return jsonify(user.to_dict()), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
@swag_from({
        'tags': ['Auth'],
        'parameters': [
            {'name': 'body', 
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'password': {'type': 'string'}
                },
                'required': ['username', 'password']
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Login successful',
            }
        }
    })
def login():
    data = request.get_json()
    result = authService.login(data['username'], data['password'])
    if not result:
        return jsonify({'message': 'Invalid credentials'}), 401
    access_token = result['access_token']
    user = result['user']
    return jsonify({
        "access_token": access_token,
        'user': user.to_dict()
    }), 200
        