from rply import LexerGenerator
from dictionary import keywords, syntax

class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()
        self.initialize_lexer()

    def build_lexer(self):
        self.lexer.build()
        return self.lexer

    def initialize_lexer(self):
        for key, value in syntax.general_tokens:
            self.lexer.add(key, value)

        for key, value in syntax.maths_tokens:
            self.lexer.add(key, value)

        for key, value in keywords.conditional_tokens:
            self.lexer.add(key, value)

        for key, value in keywords.function_tokens:
            self.lexer.add(key, value)

        for key, value in keywords.loop_tokens:
            self.lexer.add(key, value)

        for key,v alue in keywords.primitives_tokens:
            self.lexer.add(key, value)

        self.lexer.ignore('\s+')
