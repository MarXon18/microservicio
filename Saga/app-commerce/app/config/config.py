from asyncio.log import logger
from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    TESTING = False
    
    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    CACHE_REDIS_HOST = os.environ.get('REDIS_HOST')
    CACHE_REDIS_PORT = os.environ.get('REDIS_PORT')
    CACHE_REDIS_DB = os.environ.get('REDIS_DB')
    CACHE_REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
        
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

def factory(app):
    configuration = {
        'testing': TestConfig,
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    
    return configuration[app];