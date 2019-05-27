from flaskblog import app

# this allows you to run the app without "flask run"
# you can just type: "python flaskblog.py"
if __name__ == '__main__':
    app.run(debug=True)

# run in dev mode:
#export FLASK_ENV=development
