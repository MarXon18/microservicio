from datetime import datetime
from app.models import Compra
from app.repositories import CompraRepository
from app import cache

repository = CompraRepository()
class CompraService:

   def save(self, compra: Compra) -> Compra:
      compra.fecha_compra = datetime.now()
      result = repository.save(compra)
      if result:
         cache.set(f"compra_{result.id}", result, timeout=60)
      return result
   
   def delete(self, id: int) -> Compra:
      if id:
         cache.delete(f"compra_{id}")
      
      result = repository.delete(id)
      return result