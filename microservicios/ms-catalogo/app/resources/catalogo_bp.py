# app/resources/catalogo_bp.py
from flask import Blueprint, jsonify

# Definir el blueprint
catalogo_bp = Blueprint('catalogo_bp', __name__)

# Ruta de ejemplo
@catalogo_bp.route('/resource', methods=['GET'])
def get_resource():
    return jsonify(message="This is the resource endpoint"), 200

# Otra ruta de ejemplo
@catalogo_bp.route('/items', methods=['GET'])
def get_items():
    items = [
        {"id": 1, "name": "Item 1", "price": 10.0},
        {"id": 2, "name": "Item 2", "price": 20.0},
        {"id": 3, "name": "Item 3", "price": 30.0}
    ]
    return jsonify(items=items), 200
