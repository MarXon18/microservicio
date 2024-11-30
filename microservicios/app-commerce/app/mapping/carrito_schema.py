from marshmallow import fields, Schema, post_load
from app.models import Carrito

class CarritoSchema(Schema):
    producto = fields.Nested("ProductoSchema")
    direccion_envio= fields.String(required=True)
    cantidad= fields.Float(required=True)
    medio_pago= fields.String(required=True)

    @post_load
    def make_carrito(self, data, **kwargs):
        return Carrito(**data)