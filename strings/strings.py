# Different types of String using '' , "", ''' '''
# course2 = "Pyton for Beginners"
# course3 = 'pyton for"Beginners"'
# course4 = "pyton's for Beginners"
# email = '''
# Hii mosh,

# My self raj.
# Hope you are doing well and learning every day. Have a good day.

# Thank You.
# '''

# print(email)

course = 'pyton for beginners'
# if we want first char of the string use course[0]
print(course[0])  # output:- p
print(course[-1])  # output:- s
print(course[0:6])  # output:- pyton
print(course[0:-1])  # this will not print last index.
# output:- pyton for beginner "python supports negative index means -1 will give you last index"
print(course[:])
# output:- pyton for beginners  "to copy one string in another"
print(course[6:])
# output:- for beginners "it will print from index no 6 to index no string.length"
# output:- python for "it will print from index 0 till index 9"
print(course[:10])

name = 'jennifer'
# output:- ennife "it will print from index 1 till last index -1 "
print(name[1:-1])


# Formated Strings
first = "john"
last = "smith"
message = first + ' [' + last + '] is a good coder'
# concanating string but this is hard to visualize what should it print.
print(message)
msg = f'{first} [{last}] is a good coder'
# This is a formated String easy to read
# For formated string use f as prefix before string and right values in {}
print(msg)

course = "Python for Beginners"
# out:- 20 "return length of string len() fun is use for return lenth of any thing for exaple list, array, etc."
print(len(course))
print(course.upper())  # out:- PYTON FOR BEGINNERS
print(course.lower())  # out:- python for beginners
print(course.title())  # out:- Python for Beginners
print(course.find('P'))
# out:- 0 "if P is present in string it will return index of P if not return -1"
print(course.find('for'))
# out;- 7 "if for is present in list it will return index of first char that is f "
print(course.replace('P', 'J'))  # out:- Jython for Beginners
print(course.replace('Beginners', 'Absolute Beginners'))
# out:- Pyton for Absolute Beginners
print('python' in course)
# out:- False "return boolean value as python is case sensitive language"
