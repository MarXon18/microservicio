from flask import Blueprint, request

from app.mapping import StockSchema
from app.services import StockService

stock_bp = Blueprint('stock', __name__)
stock_schema = StockSchema()
stock_service = StockService()

@stock_bp.route('/inventarios/retirar', methods=['POST'])
def retirar_producto():
    stock = stock_schema.load(request.json)
    stock = stock_service.retirar(stock)
    if stock.id:
        status_code = 200 
    else:
        status_code = 500

    return stock_schema.dump(stock), status_code

@stock_bp.route('/inventarios/ingresar', methods=['POST'])
def ingresar_producto():
    stock = stock_schema.load(request.json)
    stock = stock_service.ingresar(stock)
    
    if stock.id:
        status_code = 200 
    else:
        status_code = 500

    return stock_schema.dump(stock), status_code
