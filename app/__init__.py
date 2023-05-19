from flask import Flask 
from .routes import create_routes
from .config import Config
from .data import database as db
from .extensions import init_login_manager

DB_NAME = 'database.db'

def create_app():
  app = Flask(__name__)
  
  create_routes(app)

  app.config.from_object(Config)

  db.initialize_database(app)
  
  with app.app_context():
    db.check_database('app/' + DB_NAME)

  init_login_manager(app)

  return app
