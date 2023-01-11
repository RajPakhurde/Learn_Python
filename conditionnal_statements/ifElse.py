is_hot = False
is_cold = True
# SYNTAX OF IF ELSE IN PYTHON
if is_hot:
    print("It's hot today!!")
    print("Drink plantey of water..")
elif is_cold:
    print("It's cold today!!")
    print("Wear warm clothes")
else:
    print("It's lovely day")

print("Enjoy the day!!")

price = 1000000
debit_credit = False

if debit_credit:
    downpayment = 0.1 * price
else:
    downpayment = 0.2 * price

print(f"Downpayment: ${downpayment}")
