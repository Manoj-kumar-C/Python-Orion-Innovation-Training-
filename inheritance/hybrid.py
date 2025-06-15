class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C:
    def method_c(self):
        print("Class C")

class D(B, C):  # Inherits from both B (which inherits A) and C
    def method_d(self):
        print("Class D")

obj = D()
obj.method_a()  # From A
obj.method_b()  # From B
obj.method_c()  # From C
obj.method_d()  # From D
