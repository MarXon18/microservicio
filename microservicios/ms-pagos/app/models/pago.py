from dataclasses import dataclass
import datetime
from app import db

@dataclass(init=False, repr=True, eq=True)
class Pago(db.Model):
    __tablename__ = 'pagos'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    producto: int = db.Column("producto_id", db.Integer, nullable=False)
    precio: float = db.Column(db.Float, nullable=False, default=0.0)
    medio_pago: str = db.Column(db.String(120), nullable=False)
    deleted_at: datetime = db.Column(db.DateTime, nullable=True)
