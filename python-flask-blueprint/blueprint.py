from flask import Blueprint

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/')
def index():
    return "hello world"
