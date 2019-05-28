from flask import render_template as render, flash, redirect, url_for, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been, you're now able to login", 'success')
        return redirect(url_for('home'))

    return render('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next') # here we use get() instead of [] to avoid error in case of null
            #flash('You have been logged in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull. Please check your email and password', 'danger')
    return render('login.html', title="Login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render('account.html', title="Account")
