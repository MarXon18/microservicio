from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_caching import Cache
from flask_marshmallow import Marshmallow
import os, redis
from app.config import config
from app.config.cache_config import cache_config

load_dotenv()

# Variables de entorno rutas de microservicios
CATALOGO_SERVICE_URL = os.getenv('CATALOGO_SERVICE_URL')
INVENTARIO_SERVICE_URL = os.getenv('INVENTARIO_SERVICE_URL')
PAGOS_SERVICE_URL = os.getenv('PAGOS_SERVICE_URL')
COMPRAS_SERVICE_URL = os.getenv('COMPRAS_SERVICE_URL')
MAIN_COMMERCE_COMPRA_URL = os.getenv('MAIN-COMMERCE-COMPRA_URL')

ma = Marshmallow()
cache = Cache()

def create_app() -> Flask:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    
    print(f"Running in {cache_config} mode")
    ma.init_app(app)
    cache.init_app(app, config=cache_config)
    
    from app.resources.home import home_bp
    app.register_blueprint(home_bp, url_prefix='/api/v1')
    
    @app.errorhandler(ValueError)
    def handle_value_error(error):
        return jsonify({"status": "Error", "detail": str(error)}), 400
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
