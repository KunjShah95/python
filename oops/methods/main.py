"""
#  1. Instance Methods

The most common type.

Take self as the first parameter.

Can access and modify instance variables
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
c = Circle(5)
print(c.area())


"""
2. Class Methods
Use the @classmethod decorator.

Take cls (class itself) as the first parameter instead of self.

Can access/modify class variables (shared among all instances).
"""

class Circle:
    pi = 3.14 
    
    def __init__(self, radius):
        self.radius = radius
        
    @classmethod
    def change_pi(cls, new_pi):
        cls.pi = new_pi
        
    def area(self):
        return Circle.pi * self.radius ** 2
    
Circle.change_pi(3.14159)
c = Circle(5)
print(c.area())  # Output: 78.53975

"""
3. Static Methods
Use the @staticmethod decorator.

Don’t take self or cls.

Behave like regular functions but belong to the class namespace.

Useful when function relates to the class logically but doesn’t access instance or class data.
"""

class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

print(MathHelper.add(5, 7))  # 12
