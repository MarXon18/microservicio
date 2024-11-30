from app import db
from app.models import Producto

class ProductoRepository:
    
    def find(self, id: int) -> Producto:
        result = None
        if id is not None:
            result = db.session.query(Producto).filter(Producto.id == id).one_or_none()
        return result
    