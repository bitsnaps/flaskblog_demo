from flask import render_template as render, Blueprint

errors = Blueprint('errors', __name__)

# error page handlers
#P.S. Here we use app_errorhandler instead of errorhandler so the handler
# works for the entire application not only this Blueprint
@errors.app_errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render('errors/404.html'), 404

@errors.app_errorhandler(403)
def access_denied(e):
    return render('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_server(e):
    return render('errors/500.html'), 500
