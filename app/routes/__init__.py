from . import user_auth, user_view

def create_routes(app):
  app.register_blueprint(user_auth.auth, url_prefix = '/')
  app.register_blueprint(user_view.view, url_prefix = '/')
