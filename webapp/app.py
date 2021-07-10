from flask import Flask

from webapp.hello.views import blueprint as hello_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(hello_blueprint)
    return app
