class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def hobbies(self):
        print("Mother: Painting")

class Child(Father, Mother):
    def talents(self):
        print("Child: Singing")

c = Child()
c.skills()
c.hobbies()
c.talents()
