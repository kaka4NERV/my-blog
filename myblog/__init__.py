import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.update(
        SECRET_KEY=os.getenv('SECRET_KEY', '123'),
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False),
    )

    from myblog.models import db
    db.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello boy!'

    return app
