from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
# added to be able to use @login_required decorator
login_manager.login_view = 'users.login'
# adding a CSS style to the login prompt message
login_manager.login_message_category='info'
# P.S. for gmail you may need to enable secureless opttion, checkout:
# https://myaccount.google.com/lesssecureapps
mail=Mail()

# we de that at the bottom to avoid circular  imports issue
#from flaskblog import routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
