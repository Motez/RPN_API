class RPNCalculatorException(Exception):
    """Base class for exceptions in the RPN Calculator"""

    def __init__(self, message, status_code=500):
        self.message = message
        # Response status code could be managed at the exception level
        self.status_code = status_code
        super().__init__(self.message)

class InvalidOperatorError(RPNCalculatorException):

    def __init__(self, message="Operator not supported", status_code=400):
        super().__init__(message, status_code)


class InsufficientItemsError(RPNCalculatorException):

    def __init__(self, message="You need at least 2 items to perform the operation", status_code=400):
        super().__init__(message, status_code)


class RPNDivisionByZeroError(RPNCalculatorException):

    def __init__(self, message="You can't perform the division by zero operation", status_code=403):
        super().__init__(message, status_code)
