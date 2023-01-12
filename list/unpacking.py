# UNPACKING in python

cordinates = (1, 2, 3)

# if we want to use this values in operation we simple do cordinates[0] * cordinates[1] * cordinates[2]

# in simple way we can store these values in variables
x = cordinates[0]
y = cordinates[1]
z = cordinates[2]

# To acheive this in thing in short amount of line python provides unpacking feature

x, y, z = cordinates

print(x)
print(y)
print(z)
