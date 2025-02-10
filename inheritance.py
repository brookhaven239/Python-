#Parent class/Super class/Base class
class Animal:
    def speak(self):
        print("Animal is speaking")

#Child class/Sub class/Derived class
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

class Dog(Cat):
    def bark(self):
        print("Dog is barking")

a = Animal()

c = Cat()

d = Dog()
