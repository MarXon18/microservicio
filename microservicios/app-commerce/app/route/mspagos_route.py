from flask import Blueprint, request
from app import PAGOS_SERVICE_URL
from app.services.api_requests import forward_request

# Crear Blueprint para las rutas de pagos
pagos_bp = Blueprint('pagos', __name__)

# Ruta para crear un pago (POST)
@pagos_bp.route('/', methods=['POST'])
def crear_pago():
    """Recibe una solicitud POST y la redirige al microservicio de pagos"""
    data = request.get_json()  
    url = f"{PAGOS_SERVICE_URL}/"
    return forward_request(url, request.method, data=data)

# Ruta para listar pagos (GET)
@pagos_bp.route('/', methods=['GET'])
def listar_pagos():
    """Recibe una solicitud GET y la redirige al microservicio de pagos"""
    url = f"{PAGOS_SERVICE_URL}/"
    return forward_request(url,request.method)