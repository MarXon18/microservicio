from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class Producto:
    id: int 
    nombre: str
    precio: float
    activado: bool
