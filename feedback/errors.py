class MSharpError(Exception):
    pass


class GrammarError(MSharpError):
    """Syntax error"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
