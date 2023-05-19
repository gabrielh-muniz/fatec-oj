from flask import Blueprint, render_template
from ..controller import user_controller as handler

view = Blueprint('view', __name__)

view.route('/home')(handler.home)
