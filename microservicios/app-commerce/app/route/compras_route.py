from flask import Blueprint, jsonify, request, current_app
from app.services.mspagos_service import PagoService
from app.services.msinventario_service import InventarioService
from app.services.mscatalogo_service import CatalogoService
from app.services.mscompras_service import CompraService

# Crear Blueprint para el registro de compras
registrar_compra_bp = Blueprint('registrar_compra', __name__)
compra_service = CompraService()
inventario_service = InventarioService()
pago_service = PagoService()
catalogo_service = CatalogoService()

# Ruta para realizar la compra (POST)
@registrar_compra_bp.route('/', methods=["POST"])
def registrar_compra():
    # Recibir datos json
    data = request.json
    metodo_pago = data["metodo"]
    producto_id = data["producto_id"]
    cantidad = data["cantidad"]
    direccion_envio = data["direccion_envio"]

    # Gestor de keys para bloquear el producto
    redis_client = current_app.redis_client
    lock_key = f"lock:{producto_id}"
    lock = redis_client.lock(lock_key, timeout=10)
    
    # Logica de compra
    try:
        # Obtener bloqueo del producto
        if not lock.acquire(blocking=True):
            return jsonify({"status": "Error", "detail": "Error al obtener el lock"}), 500
       
        # Verificar producto
        producto_response = catalogo_service.obtener_producto(producto_id)
        if producto_response is None:
            return jsonify({"status": "Error", "detail": "Producto no encontrado"}), 404
        
        # Verificar stock
        inventario_response = inventario_service.obtener_stock(producto_id)
        stock_disponible = inventario_response.get("stock", 0)
        if stock_disponible < cantidad:
            return jsonify({"status": "Error", "detail": "No hay suficiente stock para proceder con la compra"}), 400

        # Registrar compra
        data_compra = {
            "producto_id": producto_id,
            "cantidad": cantidad,
            "direccion_envio": direccion_envio
        }
        compra = compra_service.crear_compra(data_compra)
        compra_id = compra["compra_id"]
        if not compra or "error" in compra:
            compra_service.compensar_compra(compra_id)
            return jsonify({"status": "Error", "detail": "No se pudo crear la compra"}), 500

        # Registrar pago
        monto_total = producto_response.get("precio") * cantidad
        data_pago = {
            "monto": monto_total,
            "metodo": metodo_pago,
            "descripcion": f"Pago de la compra ID {compra_id}"
        }
        pago = pago_service.crear_pago(data_pago)
        pago_id = pago["pago_id"]
        if not pago or "error" in pago:
            pago_service.compensar_pago(pago_id)
            compra_service.compensar_compra(compra_id)
            return jsonify({"status": "Error", "detail": "No se pudo crear el pago"}), 500
        
        # Registrar transaccion
        data_transaccion = {
            "producto_id": producto_id,
            "cantidad": cantidad,
            "entrada_salida": 2
        }
        transaccion = inventario_service.registrar_venta(data_transaccion)
        transaccion_id = transaccion["transaccion_id"]
        if not transaccion or "error" in transaccion:
            inventario_service.compensar_venta(transaccion_id)
            compra_service.compensar_compra(compra_id)
            pago_service.compensar_pago(pago_id)
            return jsonify({"status": "Error", "detail": "No se pudo crear la transaccion"}), 500
    
        return jsonify({"mensaje": "Venta realizada con exito", "compra": compra, "pago": pago, "transaccion": transaccion}), 201
    finally:
        #Liberar bloqueo del producto
        lock.release()