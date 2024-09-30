#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1. Index Route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2. Print String Route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter  # Display in browser

# 3. Count Route
@app.route('/count/<int:parameter>')
def count(parameter):
    # Create a range of numbers up to the parameter and return them as a string
    numbers = "\n".join(str(i) for i in range(parameter)) + '\n'
    return numbers  # Return as plain text without <pre> tags


# 4. Math Operation Route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # Perform the operation based on the parameter
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        # Check if num2 is zero to prevent division by zero error
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    elif operation == '%':
        # Check if num2 is zero to prevent modulus by zero error
        if num2 == 0:
            return "Error: Modulus by zero is not allowed."
        result = num1 % num2
    else:
        return "Error: Unsupported operation."

    return str(result)  # Return result as plain text


if __name__ == '__main__':
    app.run(port=5555, debug=True)
