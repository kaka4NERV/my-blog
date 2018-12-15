from flask import Flask

def create_app():
    app = Flask(__name__)

    # app.config
    #
    # sql

    @app.route('/')
    def hello():
        return 'Hello boy!'
    return app

