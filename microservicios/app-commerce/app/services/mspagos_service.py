import requests
import os
import logging
from app.mapping import PagoSchema
from app.models import Pago, Producto


class ClientePagosService:
    
    def __init__(self):
        self.pago = Pago()
        self.URL = os.getenv('MSPAGOS_URL', 'http://localhost:5003/api/v1/')

    def registrar_pago(self, producto: Producto, medio_pago:str ) -> None:
        self.pago.producto = producto.id
        self.pago.precio = producto.precio
        self.pago.medio_pago = medio_pago
        pago_schema = PagoSchema()
        r = requests.post(f'{self.URL}pagos/registrar', json=pago_schema.dump(self.pago))
        if r.status_code == 200:
            logging.info(f"Pago <- {r.json()}")
           
            self.pago = pago_schema.load( r.json() )
            logging.info(f"Pago realizado id: {self.pago.id}")
        else:
            logging.error(f"Error en el microservicio compras")
            raise BaseException("Error en el microservicio compras")

    
    def cancelar_pago(self) -> None:
        
        if not self.pago.id:
            logging.error("No se puede cancelar el pago sin ID")
            raise BaseException("No se puede cancelar el pago sin ID")
        
        r = requests.put(f'{self.URL}pagos/cancelar/{self.pago.id}')
        if r.status_code == 200:
            logging.warning(f"Pago eliminado ID: {self.compra.id}")
        else:
            logging.error("Error tratando de compensar Pago")
            raise BaseException("Error tratando de compensar Pago")