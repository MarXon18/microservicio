from tenacity import retry, wait_random, stop_after_attempt
import requests
from flask import jsonify

@retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(3))
def forward_request(url, method, data=None, headers=None):
    try:
        # Realizar la solicitud al microservicio
        response = requests.request(method, url, json=data, headers=headers, timeout=5)
        
        # Retornar la respuesta del microservicio
        return response.json(), response.status_code
    
    except requests.exceptions.RequestException as e:
        # Manejo de errores en caso de no poder comunicarse con el microservicio
        return jsonify({"error": "Servicio no disponible", "detalles": str(e)}), 503