import random

random_number = random.randint(1, 50)
count = 1

for user_number in range(1,7):
    user_number = int(input("Number: "))
    if count >= 6:
        print("Try next time")
    elif user_number > random_number:
        print("Less number")
        count += 1
    elif user_number < random_number:
        print("Hight number")
        count += 1
    elif user_number == random_number:
        print("Good job!!!")
        break



