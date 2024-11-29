from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [
    {"id": 1, "nombre": "Producto 1", "stock": 10, "precio": 100},
    {"id": 2, "nombre": "Producto 2", "stock": 5, "precio": 200}
]

@app.route('/productos', methods=['GET'])
def listar_productos():
    return jsonify(productos)

@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)
    return jsonify(producto) if producto else ('', 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
