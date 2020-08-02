"""
27.03.2020
Literal string interpolation hack for python2. Just playing around.
Bogdan Prădatu
"""


class Man():
    eyes = 2
    hands = 2
    legs = 2
    nose = 1

    @classmethod
    def setupClass(cls):
        cls.species = "human"
        cls.gender = 'male'
        cls.type = "{cls.gender} {cls.species}".format(**locals())

    def __init__(self, name, age, message):
        self.name = name
        self.age = age
        self.message = f"I have {self.legs} legs and {self.eyes} eyes."
        print("{self.type} created".format(**locals()))

    def talk(self):
        print("{self.message}".format(**locals()))


Man.setupClass()
class A():
    def __init__(self):
        self.settings = Man("asda", 30, "asdad")

class B(A):
    def asd(self):
        print(f"Species: {self.settings.species}")

a = Man(name='Bogdan', age=30, message='Hello')
print("Man's first words:", end=" ")
a.talk()




