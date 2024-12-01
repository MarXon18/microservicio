# app/resources/inventarios_bp.py
from flask import Blueprint, jsonify

# Definir el blueprint
inventarios_bp = Blueprint('inventarios_bp', __name__)

# Ruta de ejemplo
@inventarios_bp.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(message="This is the inventory endpoint"), 200

# Otra ruta de ejemplo
@inventarios_bp.route('/items', methods=['GET'])
def get_items():
    items = [
        {"id": 1, "name": "Item 1", "stock": 100},
        {"id": 2, "name": "Item 2", "stock": 50},
        {"id": 3, "name": "Item 3", "stock": 200}
    ]
    return jsonify(items=items), 200
