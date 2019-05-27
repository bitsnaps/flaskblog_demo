from flask import render_template as render, flash, redirect, url_for
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Peter',
        'title': 'Flask for beginner',
        'content': 'Course of Flask',
        'date_posted': 'May 24, 2019'
    },
    {
        'author': 'Make',
        'title': 'Python for Data Science',
        'content': 'Data Science with python3',
        'date_posted': 'May 23, 2019'
    }
]

# Run the app with: "export FLASK_APP=flaskblog.py" && flask run
@app.route('/')
@app.route('/home')
def home():
    #return '<h1>Home</h1>'
    return render('home.html', posts=posts)

@app.route('/about')
def about():
    return render('about.html', title="About")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == form.password.data:
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull. Please check your username and password', 'danger')
    return render('login.html', title="Login", form=form)
