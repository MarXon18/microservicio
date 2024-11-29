import logging
from flask import Blueprint, request
from app.mapping import CompraSchema
from app.services import CompraService

compra_bp = Blueprint('compra', __name__)

compra_schema = CompraSchema()
compra_service = CompraService()

@compra_bp.route('/compras', methods=['POST'])
def comprar():
    compra = compra_schema.load(request.json)
    logging.info(f"Compra <-: {compra}")
    compra = compra_service.save(compra)
    if compra.id:
        status_code = 200
    else:
        status_code = 500
    logging.info(f"Compra ->: {compra}")
    return compra_schema.dump(compra), status_code

@compra_bp.route('/compras/<int:id>', methods=['DELETE'])   
def borrar_compra(id):
    compra = compra_service.delete(id)
    if compra.deleted_at:
        status_code = 200
    else:
        status_code = 500
    return compra_schema.dump(compra), status_code
