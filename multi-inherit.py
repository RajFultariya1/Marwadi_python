#python program for multilevel inheritance

class Animal:
    def breathe(self):
        print("Breathing...")

class Mammal(Animal):
    def walk(self):
        print("Walking on earth...")

class Dog(Mammal):
    def bark(self):
        print("Barking! Woof!")

my_dog = Dog()

my_dog.breathe()

my_dog.walk()

my_dog.bark()
