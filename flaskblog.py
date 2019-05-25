from flask import Flask, render_template as render, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# created for wtforms
# got from: python -c "import secrets; print(secrets.token_hex(16))"
app.config['SECRET_KEY'] = 'adc83dfe8f2d9416faccfca86a66d263'

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


# this allows you to run the app without "flask run"
# you can just type: "python flaskblog.py"
if __name__ == '__main__':
    app.run(debug=True)

# run in dev mode:
#export FLASK_ENV=development

# https://www.youtube.com/watch?v=UIJKdCIEXUQ&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3
