# Inheritance in python

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bhuuuuuu...")


class Cat(Mammal):
    def annotying(self):
        print("Cat is annoying..")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat = Cat()
cat.walk()
cat.annotying()
