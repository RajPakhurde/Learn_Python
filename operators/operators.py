# OPERATORS IN PYTHON
print(10 + 3)  # out:- 13
print(10 - 3)  # out:- 7
print(10 / 3)  # out:- 3.333333333
print(10 // 3)  # out:- 3 "if we want int value after division we use '//' operator"
print(10 ** 3)  # out:- 1000 "10^3"
print(10 % 3)  # out:- 1

# OPERATOR PRESEDENCE
# parentasis ()
# exponential **
# multi and div
# add and sub
ans = (2 + 3) * 10 + 20 - 2 ** 2
#  5 * 10 + 20 - 4
#  50 + 20 -4
#  70 - 4
#  66
print(f'{ans} is the final answer')


# LOGICAL OPERATORS IN PYTHON
# and , or , not
has_good_credit = True
has_good_income = False
has_criminal_record = False

if has_good_credit and has_good_income:
    print("Eligible for loan")
elif has_good_income or has_good_credit:
    print("Partially eligible")

if has_good_credit and not has_criminal_record:
    print("Eligible for laon")

# COMPARISION OPERATORS IN PYTHON   :- < , > , <= , >= , == , !=

# name = input("Enter your name? ")
# length = len(name)

# if length < 3:
#     print("Name be atleast 3 characters!")
# elif length > 10:
#     print("Name can be a maximum of 10 characters")
# else:
#     print("Looks good!")


# Exercise

weight = input("Weight: ")
l_or_k = input("(L)bs or (K)g: ").lower()

if l_or_k == 'l':
    weight = int(weight) / 2
    print(f"You are {weight} kgs")
else:
    weight = int(weight) * 2
    print(f"You are {weight} pounds")
