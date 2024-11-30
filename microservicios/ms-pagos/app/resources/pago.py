from flask import Blueprint, request

from app.mapping import PagoSchema
from app.services import PagoService

pago_bp = Blueprint('pago', __name__)
pago_schema = PagoSchema()
pago_service = PagoService()

@pago_bp.route('/pagos/registrar', methods=['POST'])
def registrar_pago():
    pago = pago_schema.load(request.json)
    result = pago_service.registrar_pago(pago)
    if result:
        status_code = 200 
    else:
        status_code = 400
    return pago_schema.dump(result), status_code

@pago_bp.route('/pagos/cancelar/<int:id>', methods=['PUT'])
def cancelar_pago(id):
    pago = pago_service.find_by_id(id)
    status_code = 400
    result = None
    if pago:
        result = pago_service.cancelar_pago(pago)
        if result:
            status_code = 200 
    
    return pago_schema.dump(result), status_code

