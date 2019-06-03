import os
import json

# for configuration on Linux Server
# with open('/etc/config.json') as config_file:
#     config = json.load(config_file)

# Those can be store to your environnement variables
# or json config file from Linux Server e.g. config.get('SQLALCHEMY_DATABASE_URI')
class Config():
    # defined with a relative path from local file
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    # hide a warning
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # created for wtforms
    # got from: python -c "import secrets; print(secrets.token_hex(16))"
    SECRET_KEY='adc83dfe8f2d9416faccfca86a66d263'

    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    # email and password are stored in the system environnement variables
    MAIL_USERNAME=os.environ.get('EMAIL_USER')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASS')
    MAIL_SENDER=os.environ.get('EMAIL_SENDER') or 'noreply@demo.com' # e.g. noreply@demo.com
