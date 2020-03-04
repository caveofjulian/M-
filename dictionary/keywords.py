conditional_tokens = {
    "if": "if",
    "elif": "elif",
    "else": "else",
    "and": "&&",
    "or": "||"
}

loop_tokens = {
    "while": "while",
    "for": "for",
    "continue": "continue",
    "break": "stop",
}

function_tokens = {
    "function": "function",
    "exposed": "exposed",  # States that a method is exposed
    "nothing": "nothing",  # No return type
    "return": "giveback",
}

primitives_tokens = {
    "number": "number",
    "string": "text",
    "character": "char",
    "boolean": "condition",
    "byte": "8bits"
}

