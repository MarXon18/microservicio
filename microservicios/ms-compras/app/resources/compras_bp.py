# app/resources/compras_bp.py
from flask import Blueprint, jsonify

# Definir el blueprint
compras_bp = Blueprint('compras_bp', __name__)

# Ruta de ejemplo
@compras_bp.route('/order', methods=['GET'])
def get_order():
    return jsonify(message="This is the order endpoint"), 200

# Otra ruta de ejemplo
@compras_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = [
        {"id": 1, "item": "Item 1", "quantity": 2},
        {"id": 2, "item": "Item 2", "quantity": 1},
        {"id": 3, "item": "Item 3", "quantity": 5}
    ]
    return jsonify(orders=orders), 200
