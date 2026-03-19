def greet(name):
    if not name:
        raise ValueError("Name must not be empty")
    return f"Hello, {name}!"


def farewell(name):
    if not name:
        raise ValueError("Name must not be empty")
    return f"Goodbye, {name}!"
