from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flasgger import swag_from

user_db = Blueprint('user_db', __name__)
@user_db.route('/me', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['User'],
    "security": [{"BearerAuth": []}],
    'responses': {
        200: {
            'description': 'Información del usuario autenticado',
            "examples": {
                "application/json": {
                    "id": 2,
                    "username": "usuario_ejemplo"
                }
            }
        },
        401: {
            'description': 'No autorizado',
        }
    }
})

def me():
    user_id = get_jwt_identity()
    claims = get_jwt()
    return jsonify({
        "id": user_id,
        "username": claims.get("username")
    }), 200