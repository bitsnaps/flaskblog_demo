import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

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
# P.S. for gmail you may need to enable secureless opttion (https://myaccount.google.com/lesssecureapps)
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
# email and password are stored in the system environnement variables
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')
app.config['MAIL_SENDER']=os.environ.get('EMAIL_SENDER') or 'noreply@demo.com' # e.g. noreply@demo.com
mail=Mail(app)

# we de that at the bottom to avoid circular  imports issue
from flaskblog import routes
