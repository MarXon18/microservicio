from flask import Blueprint, request
from app import COMPRAS_SERVICE_URL
from app.services.api_requests import forward_request

#Crear Blueprint para las rutas de pagos
compras_bp = Blueprint('compras', __name__)

# Ruta para crear una compra (POST)
@compras_bp.route('/', methods = ["POST"])
def crear_compra():
    """Recibe una solicitud POST y la redirige al microservicio de compras"""
    data = request.get_json()
    url = f"{COMPRAS_SERVICE_URL}/"
    return forward_request(url, request.method, data=data)