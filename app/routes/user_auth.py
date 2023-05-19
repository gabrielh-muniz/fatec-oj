from flask import Blueprint
from ..controller import user_controller as handler

auth = Blueprint('auth', __name__)

auth.route('/login', methods=['GET', 'POST'])(handler.login)

auth.route('/logout')(handler.logout)

auth.route('/sign-up', methods=['GET', 'POST'])(handler.sign_up)
