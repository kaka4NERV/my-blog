import time

from flask import Blueprint, render_template, g, redirect, url_for
from myblog.models import db, Post
from myblog.forms import DeleteForm, CreateForm, UpdateForm
from myblog.auth import login_required

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    form = DeleteForm()
    posts = Post.query.order_by(Post.timestamp).all()
    return render_template('index.html', posts=posts, form=form)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreateForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        post = Post(title=title, body=body, author_id=g.user.id, timestamp=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.index'))
    return render_template('create.html', form=form)


@bp.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):
    form = UpdateForm()
    post = Post.query.get(id)
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for('blog.index'))
    form.title.data = post.title
    form.body.data = post.body
    return render_template('update.html', form=form)
