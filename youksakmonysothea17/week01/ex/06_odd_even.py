number = input("Enter a number:\n")
while not (number == "exit" or number == "EXIT"):
    if number.isdigit() is True:
        number = int(number)
        if number % 2 != 0:
            print(f"{number} is ODD")
            exit()
        else:
            print(f"{number} is EVEN")
            exit()
    else:
        print(f"{number} is not a valid number.")
        number = input()
