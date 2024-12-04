from flask import Blueprint, request
from app import INVENTARIO_SERVICE_URL
from app.services.api_requests import forward_request

# Crear Blueprint para las rutas de inventario
inventario_bp = Blueprint('inventario', __name__)

# Ruta para crear un registro (POST)
@inventario_bp.route('/', methods = ["POST"])
def crear_registro():
    """Recibe una solicitud POST y la redirige al microservicio de inventario"""
    data = request.get_json()
    url = f"{INVENTARIO_SERVICE_URL}/"
    return forward_request(url, request.method, data=data)

# Ruta para obtener el stock de un producto por id (GET)
@inventario_bp.route('/<int:id>', methods = ["GET"])
def obtener_stock(id):
    """Recibe una solicitud GET y la redirige al microservicio de inventario"""
    url = f"{INVENTARIO_SERVICE_URL}/{id}"
    return forward_request(url, request.method)