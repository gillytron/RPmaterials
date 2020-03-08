#!/usr/bin/env python3

# File: mathrepl.py

"""MathREPL, a math expression evaluator using Python's eval() and math."""

import math

__version__ = "1.0"
__author__ = "Leodanis Pozo Ramos"

ALLOWED_NAMES = {name: obj for name, obj in math.__dict__.items() if "__" not in name}

PS1 = "mr>>"

WELCOME = f"""
MathREPL {__version__}, your Python math expressions evaluator!
Enter a valid math expression after the prompt "{PS1}".
Type "help" for more information.
Type "quit" or "exit" to exit.
"""

USAGE = f"""
Usage:
Build math expressions using numeric values and operators.
Use any of the following functions and constants:

{', '.join(ALLOWED_NAMES)}
"""


def evaluate(expression: str) -> float:
    """Evaluate a math expression."""
    # Compile and validate syntax
    try:
        code = compile(expression, "<string>", "eval")
    except SyntaxError:
        raise SyntaxError("Invalid input expression")

    # Validate allowed names
    for name in code.co_names:
        if name not in ALLOWED_NAMES:
            raise NameError(f'The use of "{name}" is not allowed')

    return eval(code, {"__builtins__": {}}, ALLOWED_NAMES)


def main() -> None:
    """Main loop: Read and evaluate user input."""
    print(WELCOME)
    while True:
        # Read user's input
        try:
            expression = input(f"{PS1} ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()

        # Handle special commands
        if expression.lower() == "help":
            print(USAGE)
            continue
        if expression.lower() in {"quit", "exit"}:
            raise SystemExit()

        # Evaluate the expression
        try:
            result = evaluate(expression)
        except Exception as err:
            print(err)

        # Print the result
        print(f"The result is: {result}")


if __name__ == "__main__":
    main()