import mymodule

mymodule.greet("Alice")

# another method to import 

from mymodule import greet
greet("Bob")

# Importing a module with an alias
import mymodule as mm
mm.greet("Charlie")


"""
 What is a Package?
A package is a folder containing multiple modules.

It contains an __init__.py file (can be empty) to tell Python it’s a package.
"""

def main():
    print("This runs only when the script is executed directly.")

if __name__ == "__main__":
    main()
