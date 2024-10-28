import operator

from common.exceptions import InvalidOperatorError, InsufficientItemsError, RPNDivisionByZeroError
from stack.stack import StackManager

# FIXME move this variable into config file
Allowed_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    'div': operator.truediv # To avoid URL Issues with special characters
}

class Calculator:
    """
    Calculator class to perform arithmetic operations according to an RPN calculator logic
    """

    @staticmethod
    def operate(stack_name, operator_symbol):

        op_func = Allowed_OPERATIONS.get(operator_symbol)
        if not op_func:
            raise InvalidOperatorError
        stack = StackManager.get_stack(stack_name)

        if stack.size() < 2:
            raise InsufficientItemsError

        # pop the target items
        b = stack.pop()
        a = stack.pop()

        try:
            result = op_func(a, b)
        except ZeroDivisionError:
            #FIXME pushing back the values could be delegated to DB engine transaction
            stack.push(a)
            stack.push(b)
            raise RPNDivisionByZeroError

        # update the stack
        stack.push( result)
        return result
