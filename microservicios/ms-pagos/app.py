from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/pagos', methods=['POST'])
def procesar_pago():
    data = request.get_json()
    # Procesar pago aquí (simulación)
    return jsonify({"message": "Pago procesado"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
