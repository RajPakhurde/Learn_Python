# FUNCTIONS IN PYTHON
# always define funtion before call it
# leave two lines after funtion
def greet_msg():
    print("Hello there!")
    print("Welcome onboard")


def greet_msg2(name):
    print(f"Hello {name}!")
    print("Welcome onboard")


def greet_msg3(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


print("Start")
greet_msg3("Mosh", "Velsky")
# Arguments with keys
greet_msg3(first_name="MOSH", last_name="VELSKY")
print("Finsih")

# RETURN STATEMENT IN PYTON
# by default it will return None if we don't return value from funtion


def square(number):
    return number * number


result = square(3)
print(result)


# Reorganize the emoji program using functions

emojis = {
    ":)": "😊",
    ":(": "😞"
}


def convert_emojis(msg):
    words = msg.split(' ')
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


result = convert_emojis("Today is a good day :)")
print(result)
