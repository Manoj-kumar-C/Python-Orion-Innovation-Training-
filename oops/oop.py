# 1. CLASS & OBJECT
class Animal:
    def __init__(self, name):
        self.name = name  # Encapsulation

    def speak(self):  # Polymorphism (will be overridden)
        return f"{self.name} makes a sound."


# 2. INHERITANCE
class Dog(Animal):
    def speak(self):  # Polymorphism
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):  # Polymorphism
        return f"{self.name} says Meow!"


# 3. ABSTRACTION using a base class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."


# 4. OBJECT CREATION
dog = Dog("Buddy")
cat = Cat("Whiskers")
car = Car()

# 5. OUTPUT
print(dog.speak())        # Buddy says Woof!
print(cat.speak())        # Whiskers says Meow!
print(car.start_engine()) # Car engine started.
