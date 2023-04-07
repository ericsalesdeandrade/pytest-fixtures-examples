from flask import Flask, jsonify, request
from calculator.core import Calculator

# Create the Flask application
app = Flask(__name__)

# Create the Calculator object
calculator = Calculator()

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
    result = calculator.add(a, b)
    return jsonify(result)

# Add a route for the subtract function
@app.route('/api/subtract/', methods=['POST'])
def subtract():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = calculator.subtract(a, b)
    return jsonify(result)

# Add a route for the percent function
@app.route('/api/percent/', methods=['POST'])
def percent():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = calculator.percent(a, b)
    return jsonify(result)

# Add a route for the multiply function
@app.route('/api/multiply/', methods=['POST'])
def multiply():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = calculator.multiply(a, b)
    return jsonify(result)

# Add a route for the divide function
@app.route('/api/divide/', methods=['POST'])
def divide():
    data = request.get_json()
    a = data['a']
    b = data['b']
    if b == 0:
        return jsonify("Cannot divide by zero"), 400
    result = calculator.divide(a, b)
    return jsonify(result)


if __name__ == '__main__':
    app.run()