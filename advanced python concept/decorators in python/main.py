"""A decorator is a function that modifies the behavior of another function without changing its actual code.

Think of it like wrapping a gift — you add extra behavior before or after the original function runs.

"""

from functools import wraps

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# 2. Decorators with Arguments

def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero!")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    print(f"Result: {a / b}")

divide(10, 2)   # Works fine
divide(5, 0)    # Gracefully handled


"""
     3. Using functools.wraps (Best Practice)
To preserve the original function’s name and docstring:_
    """
    

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapped function")
        return func(*args, **kwargs)
    return wrapper

"""✅ When to Use Decorators?
Logging

Authorization

Performance timing

Repeating logic across many functions (e.g., try-except, validation)

"""

