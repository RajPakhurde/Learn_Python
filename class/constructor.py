# CONSTURCTORS IN PYTHON

# we define consturctors like this def __init__(self):
# This is a method which defines constructor

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.draw()
print(point.x)  # Out:- 10
# we can change value of x and y
point.x = 11
print(point.x)  # Out:- 11


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Lets talk {self.name}")


person = Person("raj")
print(person.name)
person.talk()

bob = Person("Bob smith")
bob.talk()
