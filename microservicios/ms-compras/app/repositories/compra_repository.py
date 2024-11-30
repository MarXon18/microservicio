from app import db
from app.models import Compra

class CompraRepository:

    def save(self, compra: Compra) -> Compra:
        db.session.add(compra)
        db.session.commit()
        return compra
    
    def delete(self, id: int) -> Compra:
        compra = Compra.query.get(id)
        compra.deleted_at = db.func.now()
        db.session.commit()
        return compra