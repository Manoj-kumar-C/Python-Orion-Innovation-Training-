class Parent:
    def speak(self):
        print("Parent: Hello!")

class Child1(Parent):
    def greet(self):
        print("Child1: Hi!")

class Child2(Parent):
    def greet(self):
        print("Child2: Hey!")

c1 = Child1()
c2 = Child2()

c1.speak()
c1.greet()

c2.speak()
c2.greet()
