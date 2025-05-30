"""
    What is __init__?
The __init__ method is called automatically when an object is created.

It initializes the object's attributes.

Known as the constructor in other languages.
    """
    
#  Example: Using __init__ to Initialize Attributes

class Person:
    def __init__(self,name,age):
            self.name = name
            self.age = age
            
    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")

# Creating objects with different data
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

p1.introduce()  # My name is Alice and I'm 25 years old.
p2.introduce()  # My name is Bob and I'm 30 years old

#instance variable
"""
Variables prefixed with self. are instance variables.

Each object has its own copy of these variables.

Store object-specific data.
"""

#adding/modifying instnace variable outside the class

p1.job = "Engineer"   # Adding new attribute dynamically
print(p1.job)         # Engineer
# p2.job would raise error as it's not set
