from flask import (render_template as render, flash, redirect,
                    url_for, request, abort, Blueprint)
from flaskblog import db
from flaskblog.posts.forms import PostForm
from flaskblog.models import Post
from flask_login import current_user, login_required

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render('create_post.html', title='New Post', form=form, legend="New Post")

# @posts.route("/post/<post_id>") # works just fine
@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render('post.html', post=post)

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit() # no need to call session.add() because data here are aleady in db
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render('create_post.html', title='Update Post', form=form, legend="Update Post")


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@posts.route("/search_post", methods=['GET'])
def search_post():
    search = request.args.get('search')
    if search is None:
        return redirect(url_for('main.home'))
    return redirect(url_for('main.home', search=search))
