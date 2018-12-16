import functools

from flask import Blueprint, redirect, url_for, flash, render_template, session, g

from myblog.models import db, Admin
from myblog.forms import RegisterForm, LoginForm


bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        error = None

        if Admin.query.filter(Admin.username == username).first():
            error = 'User {} is already exists.'.format(username)

        if error is None:
            user = Admin(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))

        flash(error)
    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # remmember = form.remember.data
        error = None
        user = Admin.query.filter(Admin.username == username).first()

        if user is None:
            error = 'Incorrect username or password.'
        elif password != user.password:
            error = 'Incorrect username or password'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('blog.index'))

        flash(error)
    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('blog.index'))


@bp.before_app_request
def load_logged_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = Admin.query.filter(Admin.id == session['user_id']).first()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            redirect(url_for('auth.login'))

        return view(**kwargs)
    return wrapped_view
