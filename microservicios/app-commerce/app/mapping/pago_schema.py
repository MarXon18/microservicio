from marshmallow import validate, fields, Schema, post_load
from app.models import Pago

class PagoSchema(Schema):
    id = fields.Integer(required=False)
    producto = fields.Integer(required=False)
    precio = fields.Float(required=False)
    medio_pago = fields.String(required=False)
    deleted_at = fields.DateTime(required=False, allow_none=True)

    @post_load
    def make_pago(self, data, **kwargs):
        pago = Pago()
        for key, value in data.items():
            setattr(pago, key, value)
        return pago