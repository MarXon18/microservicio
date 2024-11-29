from app import db
from app.models import Stock
from app.repositories import StockRepository
from datetime import datetime
from app import cache

repository = StockRepository()
class StockService:
    
    def retirar(self, stock: Stock) -> Stock:
        result = None
        if stock is not None:
            stock.fecha_transaccion = stock.fecha_transaccion if stock.fecha_transaccion is not None else datetime.now()
            stock.entrada_salida = 2 # Salida de Producto
            result = repository.save(stock)
            cache.set(f'stock_{stock.id}', result, timeout=60)
        return result

    def ingresar(self, stock: Stock) -> Stock:
        result = None
        if stock is not None:
            stock.fecha_transaccion = stock.fecha_transaccion if stock.fecha_transaccion is not None else datetime.now()
            stock.entrada_salida = 1 # Entrada de Producto
            result = repository.save(stock)
            cache.set(f'stock_{stock.id}', result, timeout=60)
        return result
    

    