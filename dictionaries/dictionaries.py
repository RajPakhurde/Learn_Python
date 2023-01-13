# DICTIONARIES in PYTHON

# Dictionaries are use to store key value pairs

customer = {
    "name": "Raj Pakhurde",
    "age": 20,
    "is_verified": True
}

# we can store key values like this

print(customer["name"])  # out:- Raj Pakhurde
print(customer.get("age"))  # out:- 20
customer["birth_date"] = "4/8/2003"
print(customer.get("birth_date"))

# if key is not present in dictionarie and we use [] to access the value it will give an error

# But if we use .get() to access the value than it will return None

# out:- None , because key = "abc" is not present in dictionarie
print(customer.get("abc"))

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

phone = input("Phone: ")
i = 0
while i < len(phone):
    print(numbers.get(phone[i]))
    i += 1
# out:- one
    # two
    # three

output = ""
for ch in phone:
    output += numbers.get(ch, "!") + " "
print(output)

# convert emojis

message = input("> ")
words = message.split(' ')
output = ""

emojis = {
    ":)": "😊",
    ":(": "😞"
}

for word in words:
    output += emojis.get(word, word) + " "

print(output)
