#class is a blueprint to create objects.it defines attributes and methods that the created objects will have.
class Dog:
    def bark(self):
        print("Woof!")

# Create object (instance) of class Dog
my_dog = Dog()
my_dog.bark()   # Output: Woof!

"""
 What is an Object?
An object is an instance of a class.

You create objects to use the class’s data and methods.

🔹 The self Parameter
self represents the instance itself.

Must be the first parameter in all instance methods.

Allows access to attributes and methods of the object.
    """
    
    #adding attributes to the class
    
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")    
        
# Create object (instance) of class Dog
my_dog = Dog("Buddy")
my_dog.bark()   # Output: Buddy says Woof!