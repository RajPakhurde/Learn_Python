# Class in Python
# Classes is nothing but collection of methods and properties.

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# Object of class / instance of the class
point1 = Point()
# we can create new variables for this object but we  cannot access this variables from different objects
point1.x = 10
point1.y = 20
print(point1.x)
point2 = Point()
# print(point2.x)  It will give an error each object is new instance of that class.
point1.draw()
