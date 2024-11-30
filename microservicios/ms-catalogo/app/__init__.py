from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
import os
from app.config import config
from flask_caching import Cache
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config.cache_config import cache_config

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cache = Cache()

def create_app() -> None:

    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)

    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app, config=cache_config)
    
    from app.resources import catalogo_bp
    app.register_blueprint(catalogo_bp, url_prefix='/api/v1')
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
