from dataclasses import dataclass
import datetime

@dataclass(init=False, repr=True, eq=True)
class Pago:
    id: int
    producto: int
    precio: float
    medio_pago: str
    deleted_at: datetime
