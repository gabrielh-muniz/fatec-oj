from flask_sqlalchemy import SQLAlchemy
from os import path

database = SQLAlchemy()

def initialize_database(app):
  database.init_app(app)

def check_database(db_name):
  if not path.exists(db_name):
    database.create_all()
