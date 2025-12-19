class Animal:
    def __init__(self, n):
        self.n = n
    
    def make_sound(self):
        print("Животное издает звук")

class Dog(Animal):
    def make_sound(self):
        print("Гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

def chorus(list_a):
    for a in list_a:
        a.make_sound()

list_a = [Dog("Sharik"), Cat("Matroskin")]
chorus(list_a)
