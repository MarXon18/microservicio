# app/resources/pagos_bp.py
from flask import Blueprint, jsonify

# Definir el blueprint
pagos_bp = Blueprint('pagos_bp', __name__)

# Ruta de ejemplo
@pagos_bp.route('/payment', methods=['GET'])
def get_payment():
    return jsonify(message="This is the payment endpoint"), 200

# Otra ruta de ejemplo
@pagos_bp.route('/payments', methods=['GET'])
def get_payments():
    payments = [
        {"id": 1, "amount": 100.0, "status": "completed"},
        {"id": 2, "amount": 200.0, "status": "pending"},
        {"id": 3, "amount": 300.0, "status": "failed"}
    ]
    return jsonify(payments=payments), 200
