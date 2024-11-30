from marshmallow import fields, Schema, post_load
from app.models import Compra

class CompraSchema(Schema):
    id = fields.Integer(required=False)
    producto = fields.Integer(required=False)
    fecha_compra = fields.DateTime(required=False)
    direccion_envio = fields.String(required=True)
    deleted_at = fields.DateTime(required=False, allow_none=True)

    @post_load
    def make_compra(self, data, **kwargs):
        compra = Compra()
        for key, value in data.items():
            setattr(compra, key, value)
        return compra
        