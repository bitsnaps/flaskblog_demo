from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# defined with a relative path from local file
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
# hide a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# created for wtforms
# got from: python -c "import secrets; print(secrets.token_hex(16))"
app.config['SECRET_KEY'] = 'adc83dfe8f2d9416faccfca86a66d263'

db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
# added to be able to use @login_required decorator
login_manager.login_view = 'login'
# adding a CSS style to the login prompt message
login_manager.login_message_category='info'

# we de that at the bottom to avoid circular imports issue
from flaskblog import routes
