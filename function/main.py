def greet():
    print("Hello, world!")
    
greet()

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

def add(a, b):
    return a + b

result=add(5, 3)
print(f"Sum: {result}")

def say_hello():
    print("Hi")
x= say_hello()
print(x) # This will print None because say_hello does not return anything


# Add documentation inside triple quotes """ """ right after function definition:
def greet(name):
    """ Prints a greeting message to the user."""
    
    print(f"Hello, {name}!")
    
help(greet)  # This will show the documentation string for the greet function

#positional arguments

def greet(name, age):
    """ Prints a greeting message with name and age."""
    
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice", 30)  # Positional arguments

greet(age=25, name="Bob")  # Keyword arguments (order doesn't matter)

def greet(name, age=30):
    print(f"{name} is {age} years old.")

greet("Bob")          # age defaults to 30
greet("Alice", 25)    # age is 25

# Variable-length arguments *args
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2))           # 3
print(add(1, 2, 3, 4, 5))  # 15


# Keyword variable-length arguments **kwargs
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Alice", age=25, city="NY")
