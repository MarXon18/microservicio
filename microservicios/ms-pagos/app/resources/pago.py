from flask import Blueprint, request, jsonify
from marshmallow.exceptions import ValidationError
from app.mapping import PagoSchema
from app.services import PagoService

pago_bp = Blueprint('pago', __name__)
pago_schema = PagoSchema()
pago_service = PagoService()

@pago_bp.route('/pagos/registrar', methods=["POST", "GET"])
def registrar_pago():
    data = request.get_json()
    if not request.is_json:
        return jsonify({'error': 'La solicitud no contiene datos JSON'}), 400

    try:
        # Validar y cargar los datos
        pago = pago_schema.load(data)
        # Procesar el pago
        result = pago_service.registrar_pago(pago)
        if result:
            return jsonify({'message': 'Pago registrado correctamente'}), 200
        else:
            return jsonify({'error': 'Error al registrar el pago'}), 400
    except ValidationError as ve:
        return jsonify({'error': 'Error de validación', 'detalles': ve.messages}), 400
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor', 'detalles':str(e)}),500

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


    
    return pago_schema.dump(result), status_code

