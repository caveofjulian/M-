from sys import *
from dictionary import syntax
import pathlib
import re

file_extension = "m#"


def run(file_path):
    """Runs the file path as a M# application"""
    def interpret(file):
        if pathlib.Path(file).suffix is not ".m#":
            raise

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
        return line[0:line.find(syntax.comment_prefix)]

    src = interpret(file_path)

