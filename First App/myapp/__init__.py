# myapp/__init__.py
from flask import Flask
from flask_login import LoginManager
from .models import db , User
from .auth.routes import auth
from .home.routes import home
from .blog.routes import blog
from .todo.routes import todo
from .config import Config

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(blog, url_prefix='/blog')
    app.register_blueprint(todo, url_prefix='/todo')

    app.register_blueprint(home, url_prefix='/')

    with app.app_context():
        db.create_all()  # create tables if not exist

    return app

# # This tells Flask-Login how to get a user by ID
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))