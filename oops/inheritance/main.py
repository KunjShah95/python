"""
    Inheritance allows a class to inherit properties and methods from another class (parent/base class), enabling code reuse and hierarchies.
    """
    
class Animal:
    def speak(self):
        print("Animal speaks")
        
class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Dog barks")
    
d=Dog()
d.speak()  # Inherited method from Animal


"""
Child class inherits all methods/attributes of parent.

Child can override parent methods (like speak above).

Child can add its own methods and attributes.

"""

# using parent method 
# use super() to call parent methods

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Initialize parent attributes
        self.breed = breed

    def speak(self):
        super().speak()          # Call parent speak()
        print(f"{self.name} barks")

d = Dog("Buddy", "Labrador")
d.speak()


"""
Benefits of Inheritance:
Avoid code duplication

Establish relationships between classes

Override behavior for specific subclasses
"""

