from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from stack.stack import StackManager

stack_ns = Namespace("stack", description="Operations related to stack management")

stack_model = stack_ns.model('Stack', {
    'stack_id': fields.String(description='Unique identifier for the stack')
})

value_model = stack_ns.model('Value', {
    'value': fields.Float(description='Value to be pushed into the stack', required=True)
})

# ADD a new stack
@stack_ns.route('/')
class StackCreate(Resource):
    @stack_ns.response(200, 'Stack created successfully')
    @stack_ns.marshal_with(stack_model)
    def post(self):
        """Create a new stack"""
        stack_name = StackManager.create_stack()
        return {"stack_id": stack_name}, 200

# Get stack details
@stack_ns.route('/<string:stack_name>')
@stack_ns.param('stack_name', 'The unique identifier of the stack')
class StackRetrieve(Resource):

    @stack_ns.response(200, 'Stack retrieved successfully')
    @stack_ns.response(404, 'Stack not found')
    def get(self, stack_name):
        """Retrieve items from a stack"""
        stack = StackManager.get_stack(stack_name)
        if stack:
            return jsonify({"stack": stack.get_items()})
        return jsonify({"error": "Stack not found"}), 404

@stack_ns.route('/<string:stack_name>/push')
@stack_ns.param('stack_name', 'The unique identifier of the stack')
class StackPush(Resource):
    @stack_ns.expect(value_model)
    @stack_ns.response(200, 'Value pushed successfully')
    @stack_ns.response(400, 'No value provided')
    @stack_ns.response(404, 'Stack not found')
    def post(self, stack_name):
        """Push a value onto the stack"""
        value = request.json.get('value')
        if value is None:
            return jsonify({"error": "No value provided"}), 400

        target_stack = StackManager.get_stack(stack_name)
        if target_stack:
            target_stack.push(float(value))
            return jsonify({"message": "Value pushed successfully"})
        return jsonify({"error": "Stack not found"}), 404
