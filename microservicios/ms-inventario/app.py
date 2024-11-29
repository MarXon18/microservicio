from flask import Flask, jsonify, request

app = Flask(__name__)

inventario = [
    {"id": 1, "stock": 10},
    {"id": 2, "stock": 5}
]

@app.route('/inventario/<int:id>', methods=['PUT'])
def actualizar_inventario(id):
    data = request.get_json()
    producto = next((p for p in inventario if p["id"] == id), None)
    if producto:
        producto["stock"] = data["stock"]
        return jsonify({"message": "Inventario actualizado"})
    return ('', 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
