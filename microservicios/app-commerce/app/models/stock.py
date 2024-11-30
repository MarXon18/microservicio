from dataclasses import dataclass
import datetime


@dataclass(init=False, repr=True, eq=True)
class Stock:
    id: int 
    producto: int
    fecha_transaccion: datetime
    cantidad: float
    entrada_salida: int