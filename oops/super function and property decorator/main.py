""" 1. super() Function
Used to call methods from a parent class inside a child class.
Useful especially in inheritance when you want to extend or reuse parent methods."""

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Animal: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent __init__
        self.breed = breed

    def info(self):
        super().info()          # Call parent info()
        print(f"Breed: {self.breed}")

d = Dog("Buddy", "Labrador")
d.info()


"""
        2. @property Decorator
Allows you to use methods like attributes.

Useful for controlled access or computed attributes without changing the external interface.


        """
        
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(rect.area)  # 50 — accessed like an attribute, but computed dynamically

#  Setter with @property
# You can also define a setter to control assignment:

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value

t = Temperature(25)
print(t.celsius)  # 25
try:
    t.celsius = -300  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
