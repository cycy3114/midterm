def run(*args):
    if len(args) != 1:
        raise ValueError("Square operation requires exactly one argument.")
    try:
        value = float(args[0])
        return value ** 2
    except ValueError:
        raise ValueError("Invalid input. Please provide a numeric value.")

