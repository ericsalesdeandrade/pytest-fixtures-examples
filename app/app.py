from flask import Flask, jsonify, request
from calculator.core import Calculator

# Create the Flask application
app = Flask(__name__)

# Create the routes
@app.route('/')
def index():
    return 'Index Page'

# Add a route for the add function
@app.route('/api/add/', methods=['POST'])
def add():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = Calculator(a, b).add()
    return jsonify(result)

# Add a route for the subtract function
@app.route('/api/subtract/', methods=['POST'])
def subtract():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = Calculator(a, b).subtract()
    return jsonify(result)

# Add a route for the multiply function
@app.route('/api/multiply/', methods=['POST'])
def multiply():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = Calculator(a, b).multiply()
    return jsonify(result)

# Add a route for the divide function
@app.route('/api/divide/', methods=['POST'])
def divide():
    data = request.get_json()
    a = data['a']
    b = data['b']
    if b == 0:
        return jsonify("Cannot divide by zero"), 400
    result = Calculator(a, b).divide()
    return jsonify(result)


if __name__ == '__main__':
    app.run()