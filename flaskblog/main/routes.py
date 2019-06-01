from flask import render_template as render, request, flash, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

# Run the app with: "export FLASK_APP=flaskblog.py" && flask run
@main.route('/')
@main.route('/home')
def home():
    #return '<h1>Home</h1>'
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search')
    if search is not None:
        posts = Post.query.filter(Post.title.ilike(f"%{search}%")).order_by(
            Post.date_posted.desc()).paginate()
    else:
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    if posts.total == 0:
        flash('Sorry! We could not find any post.', 'info')
    return render('home.html', posts=posts)

@main.route('/about')
def about():
    return render('about.html', title="About")

# error page handlers
@main.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render('404.html'), 404

@main.errorhandler(403)
def access_denied(e):
    return render('403.html'), 403
