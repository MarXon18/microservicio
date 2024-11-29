from flask import Flask, jsonify, request

app = Flask(__name__)

compras = []

@app.route('/compras', methods=['POST'])
def registrar_compra():
    data = request.get_json()
    compras.append(data)
    return jsonify({"message": "Compra registrada"}), 201

@app.route('/compras', methods=['GET'])
def listar_compras():
    return jsonify(compras)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
