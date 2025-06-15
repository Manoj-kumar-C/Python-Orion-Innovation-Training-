class Grandparent:
    def home(self):
        print("Grandparent: Owns a farmhouse")

class Parent(Grandparent):
    def car(self):
        print("Parent: Owns a car")

class Child(Parent):
    def bike(self):
        print("Child: Owns a bike")

c = Child()
c.home()
c.car()
c.bike()
