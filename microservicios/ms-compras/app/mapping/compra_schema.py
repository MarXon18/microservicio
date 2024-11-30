from marshmallow import fields, Schema, post_load
from app.models import Compra

class CompraSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto = fields.Integer(required=True)
    fecha_compra = fields.DateTime(required=False)
    direccion_envio = fields.String(required=True)
    deleted_at = fields.DateTime(dump_only=True)

    @post_load
    def make_compra(self, data, **kwargs):
        return Compra(**data)