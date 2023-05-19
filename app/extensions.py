from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .data.database import database
from .models.User import User

bcrypt = Bcrypt()
login_manager = LoginManager()

def init_login_manager(app):
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))

