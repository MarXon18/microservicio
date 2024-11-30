from flask import jsonify, Blueprint, request

from app.mapping import CarritoSchema, ProductoSchema
from app.services import CommerceService

home = Blueprint('home', __name__)
carrito_schema = CarritoSchema()
producto_schema = ProductoSchema()

@home.route('/commerce/comprar', methods=['POST'])
def index():
    commerce = CommerceService()
    carrito = carrito_schema.load(request.get_json())
    commerce.comprar(carrito)
    resp = jsonify({"microservicio": "Orquestador", "status": "ok"})
    resp.status_code = 200
    return resp

@home.route('/commerce/consultar/catalogo/<int:id>', methods=['GET'])
def consultar_catalogo(id:int):
    commerce = CommerceService()
    producto = commerce.consultar_catalogo(id)
    result = {"message": "No se encontró el producto"}
    status_code = 404
    if producto:
        result = producto_schema.dump(producto)
        status_code = 200
    return result, status_code
