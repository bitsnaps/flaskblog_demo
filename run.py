from flaskblog import create_app

# Used to inject debug to templates (http://flask.pocoo.org/docs/1.0/templating/#context-processors)
# @app.context_processor
# def inject_debug():
#     return dict(debug=app.debug)

app = create_app()

# this allows you to run the app without "flask run"
# you can just type: "python flaskblog.py"
if __name__ == '__main__':
    app.run(debug=True)

# run in dev mode:
#export FLASK_ENV=development
