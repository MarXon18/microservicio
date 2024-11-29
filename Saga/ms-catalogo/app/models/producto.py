from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Producto(db.Model):
    __tablename__ = 'catalogo'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(120), unique=True, nullable=False)
    precio: float = db.Column(db.Float, nullable=False, default=0.0)
    activado: bool = db.Column(db.Boolean, default=True)
