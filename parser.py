from rply import ParserGenerator
from ast import Number, Sum, Sub, Print

from feedback.errors import GrammarError


def find_body(source, index, opening, closing):
    open_pairs = 1

    for i in range(index+1, len(source)):
        if source[i] is opening:
            open_pairs = open_pairs + 1
        elif source[i] is closing:
            if open_pairs is 1:
                return source[index+1:i]
            open_pairs = open_pairs - 1

    return None


