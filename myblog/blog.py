import time

from flask import Blueprint, render_template, g, redirect, url_for
from myblog.models import db, Post
from myblog.forms import DeleteForm, CreateForm, UpdateForm
from myblog.auth import login_required

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', posts=posts)


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
    form1 = UpdateForm()
    form2 = DeleteForm()
    post = Post.query.get(id)
    if form1.validate_on_submit():
        post.title = form1.title.data
        post.body = form1.body.data
        db.session.commit()
        return redirect(url_for('blog.index'))
    form1.title.data = post.title
    form1.body.data = post.body
    return render_template('update.html', form1=form1, form2=form2, post=post)

@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.index'))