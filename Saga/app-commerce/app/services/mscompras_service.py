import os
import logging
import requests

from app.mapping import CompraSchema
from app.models import Compra, Producto

class ClienteComprasService:
    
    def __init__(self):
        self.compra = Compra()
        self.URL = os.getenv('MSCOMPRAS_URL', 'http://localhost:5002/api/v1/')
    
    def comprar(self, producto: Producto, direccion_envio: str) -> None:
        self.compra.producto = producto.id
        self.compra.direccion_envio = direccion_envio
        compra_schema = CompraSchema()
        r = requests.post(f'{self.URL}compras', json=compra_schema.dump(self.compra))

        if r.status_code == 200:
            logging.info(f"Compra <- {r.json()}")
           
            self.compra = compra_schema.load( r.json() )
            logging.info(f"Compra realizada id: {self.compra.id}")
        else:
            logging.error(f"Error en el microservicio compras")
            raise BaseException("Error en el microservicio compras")

    def cancelar_compra(self) -> None:
        
        if not self.compra.id:
            logging.error("No se puede cancelar una compra sin id")
            raise BaseException("No se puede cancelar una compra sin id")
        
        r = requests.delete(f'{self.URL}compras/{self.compra.id}')
        if r.status_code == 200:
            logging.warning(f"Compra eliminada id: {self.compra.id}")
        else:
            logging.error("Error tratando de compensar Compras")
            raise BaseException("Error tratando de compensar Compras")