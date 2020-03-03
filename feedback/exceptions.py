class MSharpExceptions(Exception):
    """Base class for exceptions in this module."""
    pass


class NotSupportedException(MSharpExceptions):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
