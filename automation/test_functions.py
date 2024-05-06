# routes.py

from flask import Blueprint

# Create a Blueprint instance
bp = Blueprint('routes', __name__)

# Define a route and a view function
@bp.route('/hello')
def hello():
    return 'Hello from another file!'