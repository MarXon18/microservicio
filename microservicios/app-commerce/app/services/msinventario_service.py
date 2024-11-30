import logging
import os
import requests

from app.mapping import StockSchema
from app.models import Stock
from app.models.carrito import Carrito

class ClienteInventarioService:
    
    def __init__(self):
        self.stock = Stock()
        self.URL = os.getenv('MSINVENTARIOS_URL', 'http://localhost:5004/api/v1/')
    
    def retirar_producto(self, carrito: Carrito) -> None:
        self.stock.producto = carrito.producto.id
        self.stock.cantidad = carrito.cantidad
        self.stock.entrada_salida = 2
        stock_schema = StockSchema()
        r = requests.post(f'{self.URL}inventarios/retirar', json=stock_schema.dump(self.stock))

        if r.status_code == 200:
            logging.info(f"Stock <- {r.json()}")
           
            self.stock = stock_schema.load( r.json() )
            logging.info(f"Stock registrado id: {self.stock.id}")
        else:
            logging.error(f"Error en el microservicio Stock")
            raise BaseException("Error en el microservicio Stock")

    def ingresar_producto(self) -> None:
        
        if not self.stock.id:
            logging.error("No se puede ingresar Stock sin id")
            raise BaseException("No se puede ingresar Stock sin id")
        
        self.stock.entrada_salida = 1
        r = requests.delete(f'{self.URL}inventarios/ingresar{self.stock.id}')
        if r.status_code == 200:
            logging.warning(f"Stock registrado id: {self.stock.id}")
        else:
            logging.error("Error tratando de compensar Stock")
            raise BaseException("Error tratando de compensar Stock")