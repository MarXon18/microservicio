from datetime import datetime
from flask import logging
from app import db
from app.models import Pago
from app.repositories import PagoRepository
from app import cache

repository = PagoRepository()
class PagoService:
    
    def find_by_id(self, id: int) -> Pago:
        return repository.find_by_id(id)
    
    def registrar_pago(self, pago: Pago) -> Pago:
        result = None
        try:
            result = repository.save(pago)
            cache.set(f'pago_{result.id}', result, timeout=60)
        except Exception as e:
            logging.error(f'{e}')
        return result
    
    def cancelar_pago(self, pago: Pago) -> Pago:
        result = None
        try:
            pago.deleted_at = datetime.now()
            result = repository.save(pago)
            cache.delete(f'pago_{result.id}')
        except Exception as e:
            logging.error(f'cancelando pago: {e}')
        return result