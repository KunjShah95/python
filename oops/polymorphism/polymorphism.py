"""Polymorphism with Functions
You can write functions that work with different object types if they have the same method names (Duck Typing).
"""

class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Woof")
        
def make_sound(animal):
        animal.sound()

make_sound(Cat())  # Meow
make_sound(Dog())  # Woof
