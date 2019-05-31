import random

result = 0
intro_message = "Welcome to the dices game!"

print(intro_message)
dices = input("Enter the number of dices you want to roll: ")
check_digit = dices.isdigit()

if check_digit is False or len(dices) == 0:
    print("USAGE: The number must be between 1 and 8")
    dices = input("Enter the number of dices you want to roll: ")

elif int(dices)< 1 or int(dices) > 8:
    print("USAGE: The number must be between 1 and 8")
    dices = input("Enter the number of dices you want to roll: ")

else:
    dices = int(dices)

    if dices == 1:
        print(f"RESULT: {random.randrange(1, 6)}")
    else:

        for i in range(0, dices):
            random_number = random.randrange(1, 6)
            result += random_number
            print(f"Dice {i +1}: {random_number}")
            
        print("==========")
        print(f"RESULT: {result}")
        print("==========")





