from flask import jsonify
from flask_restx import Namespace, Resource
from calculator.calculator import Calculator
from  common.exceptions import RPNCalculatorException

calculator_ns = Namespace("calculator", description="RPN Calculation")

@calculator_ns.route('/rpn/<string:op>/<string:stack_id>')
@calculator_ns.param('op', 'The operator (+, -, *, div)')
@calculator_ns.param('stack_id', 'Stack ID')
class CalculatorOperate(Resource):
    @calculator_ns.response(200, 'Operation successful')
    @calculator_ns.response(400, 'Invalid operation or insufficient items')
    @calculator_ns.response(403, 'Division by zero')
    def post(self, op, stack_id):

        """Perform an arithmetic operation on the stack"""

        try:
            result = Calculator.operate(stack_id, op)
            return jsonify({"result": result}), 200

        except RPNCalculatorException as e :
            return jsonify({"error": e.message }), e.status_code


