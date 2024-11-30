from flask import Blueprint

from app.mapping import ProductoSchema
from app.services import ProductoService

catalogo_bp = Blueprint('catalogo', __name__)
producto_schema = ProductoSchema()
producto_service = ProductoService()

@catalogo_bp.route('/catalogo/productos/<int:id>', methods=['GET'])
def get_producto(id: int):
    result = producto_schema.dump(producto_service.find(id))
    if result:
        status_code = 200 
    else:
        status_code = 404
    return result, status_code

