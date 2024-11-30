from app import db
from app.models import Pago

class PagoRepository:
    
    def find_by_id(self, id: int) -> Pago:
        return db.session.query(Pago).filter(Pago.id == id).one_or_none()
    
    def save(self, pago: Pago) -> Pago:
        db.session.add(pago)
        db.session.commit()
        return pago
    