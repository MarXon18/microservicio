from dataclasses import dataclass
import datetime

@dataclass(init=False, repr=True, eq=True)
class Compra:
    id: int
    producto: int
    fecha_compra: datetime.datetime
    direccion_envio: str
    deleted_at: datetime