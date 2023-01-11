# Loops in  python
i = 1
while i <= 5:
    print("*" * i)
    i = i+1

print("done")

# Guess Number game..
correct_num = 9
i = 1
while i <= 3:
    i = i+1
    guess = int(input("Guess: "))
    if guess != 9:
        print("Not correct")
    elif guess == 9:
        print("You won!!")
    else:
        print("You wasted 3 chances!!")


# Car game..
car_started = False
while True:
    cmd = input("> ").lower()

    if cmd == "help":
        print("Start - to start the car. \nStop - to stop the car. \nquit - to exit.")
    elif cmd == 'start':
        if car_started:
            print("Car is already started..")
        else:
            car_started = True
            print("Car started...")
    elif cmd == 'stop':
        if not car_started:
            print("Car is already stopped")
        else:
            car_started = False
            print("Car stopped..")
    elif cmd == 'quit':
        print("Game Over.")
        break
    else:
        print("Wrond command!!")

# FOR LOOP IN PYTHON

for i in 'Python':
    print(i)
# out:- P Y T H O N

for i in ['Mosh', 'raj', 'sanmesh']:
    print(i)
# out:- Mosh raj sanmesh

for i in range(10):
    print(i)
# out:- it will print 0 to 9

for i in range(5, 10):
    print(i)
# out :- it will print 5 to 9

for i in range(1, 10, 2):
    print(i)
# out:- it will print 1 3 5 7 9

price = [10, 20, 30]
ans = 0
for i in price:
    ans += i
print(ans)

# NESTED FOR LOOP

for i in range(4):
    for j in range(3):
        print(f"({i},{j})")

numbers = [5, 2, 5, 2, 2]

for i in numbers:
    print("X" * i)
