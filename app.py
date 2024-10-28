from flask import Flask
from flask_restx import Api

from stack.route import stack_ns
from calculator.route import calculator_ns

app = Flask(__name__)
api = Api(app, title="RPN Calculator API", version="1.0", description="API for a Reverse Polish Notation Calculator")

api.add_namespace(stack_ns, path="/stack")
api.add_namespace(calculator_ns, path="/calculator")

if __name__ == '__main__':
    app.run(debug=True)