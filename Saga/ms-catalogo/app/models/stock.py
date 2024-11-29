from dataclasses import dataclass
import datetime
from app import db

@dataclass(init=False, repr=True, eq=True)
class Stock(db.Model):
    __tablename__ = 'inventarios'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    producto: int = db.Column("producto_id", db.Integer, nullable=False)
    fecha_transaccion: datetime = db.Column(db.DateTime, nullable=False)
    cantidad: float = db.Column(db.Float, nullable=False, default=0.0)
    entrada_salida: int = db.Column(db.Integer, nullable=False, default=1)