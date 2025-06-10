# Class and Object

class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):  # Method
        print(f"Hello, I am {self.name} and I am {self.age} years old.")

# Creating an object
p1 = Person("Manoj", 21)
p1.greet()
