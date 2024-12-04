from flask import Blueprint, request
from app import CATALOGO_SERVICE_URL
from app.services.api_requests import forward_request

# Crear Blueprint para las rutas de catalogo
catalogo_bp = Blueprint('catalogo', __name__)

# Ruta para crear un producto (POST)
@catalogo_bp.route('/', methods=['POST'])
def crear_producto():
    """Recibe una solicitud POST y la redirige al microservicio de catalogo"""
    data = request.get_json()
    url = f"{CATALOGO_SERVICE_URL}/"
    return forward_request(url, request.method, data=data)

# Ruta para obtener un producto por id (GET)
@catalogo_bp.route('/<int:id>', methods = ['GET'])
def get_product(id):
    """Recibe una solicitud GET y la redirige al microservicio de catalogo"""
    url = f"{CATALOGO_SERVICE_URL}/{id}"
    return forward_request(url, request.method)