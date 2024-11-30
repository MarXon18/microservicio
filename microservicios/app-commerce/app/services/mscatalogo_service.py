import os
import requests
from app.models import Producto
from app.mapping import ProductoSchema
producto_schema = ProductoSchema()

class ClienteCatalogoService:

    def __init__(self):
        self.URL = os.getenv('MSCATALOGO_URL', 'http://localhost:5001/api/v1/')
    
    def obtener_producto(self, id: int) -> Producto:
        result = None
        r = requests.get(f'{self.URL}catalogo/productos/{id}')
        if r.status_code == 200:
            result = producto_schema.load(r.json())
        else:
            raise BaseException("Error en el servicio 1")
        return result