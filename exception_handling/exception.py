# EXCEPTION HANDLING IN PYTHON

try:
    age = int(input("Age: "))
    print(age)
    income = 1000
    risk = income / age
except ZeroDivisionError:
    print("Age can't be 0")
except ValueError:
    print("Invalid Value")
