"""✅ Topic 3: Closures in Python
A closure is a function object that remembers values in its enclosing scope even if that scope is no longer active.

In simple words:

A closure lets an inner function remember and access variables from its outer function, even after the outer function is finished"""

def outer_function(msg):
    def inner_function():
        print(f"Message: {msg}")
    return inner_function  # Notice we're returning the function, not calling it

my_func = outer_function("Hello from closure!")
my_func()  # Output: Message: Hello from closure!


#🔹 Practical Use Case: Making Custom Functions

def multiplier(factor):
    def multiply_by(x):
        return x * factor
    return multiply_by

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

"""
When Are Closures Useful?
When writing decorators

For data hiding

To generate specialized functions

In functional programming"""

