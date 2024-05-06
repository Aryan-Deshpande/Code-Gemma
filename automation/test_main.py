# app.py

from flask import Flask
from test_functions import bp as routes_bp  # Import the Blueprint instance

# Create a Flask application instance
app = Flask(__name__)

# Register the Blueprint instance with the Flask application
app.register_blueprint(routes_bp)

# Define a route and a view function in the main file (optional)
@app.route('/')
def index():
    return 'Welcome to the main page!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
