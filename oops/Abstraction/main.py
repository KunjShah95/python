"""
    Abstraction
Abstraction means hiding complex implementation details and showing only the necessary parts.

In Python, we often implement abstraction using abstract base classes (abc module) or just by providing a clean interface.

    """
    
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

c = Car()
m = Motorcycle()
c.start_engine()  # Car engine started
m.start_engine()  # Motorcycle engine started
