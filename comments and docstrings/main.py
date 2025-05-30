#this is a single line comment
name="Bob"  # This is a comment explaining the variable


'''
this is a multi line coomment.
it helps explain the bigger sections of code.
'''

print(name)  # Output the name variable


def greet():
    """this function prints a greeting message."""
    
    print("Hello, World!")  # Print a greeting message
    
    greet()  # Call the greet function
    
    print(greet.__doc__)  # Print the docstring of the greet function and access the docstring 