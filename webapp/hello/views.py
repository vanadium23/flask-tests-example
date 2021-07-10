from flask import Blueprint

from webapp.hello.logic import format_hello

blueprint = Blueprint('hello', __name__, url_prefix='/hello')


@blueprint.route('/<name>/')
def hello_route(name):
    return format_hello(name)


@blueprint.route('/privet/')
def privet_route():
    return "Privet!"
