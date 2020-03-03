from sys import *
from dictionary import syntax


def interpret(file):
    source = ""

    with open(file, 'r') as stream:
        for content in stream:
            content = content.lower().strip()
            if syntax.comment_prefix in content:
                content = remove_comment(content)
            if content:
                source.append(content)

    return source


def remove_comment(line):
    return line.sub(0, line.find(syntax.comment_prefix))

