from marshmallow import validate, fields, Schema, post_load
from app.models import Pago

class PagoSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto = fields.Integer(required=True)
    precio = fields.Float(required=True)
    medio_pago = fields.String(required=True)
    deleted_at = fields.DateTime(dump_only=True)

    @post_load
    def make_pago(self, data, **kwargs):
        return Pago(**data)