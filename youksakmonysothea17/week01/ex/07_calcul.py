number = input("Enter a number: ")
total = 0

while number != "exit":

    if number.isdigit() or number[0] == '-':
        total += int(number)
        print("TOTAL:", total)

    else:
        total = total
        print("TOTAL:", total)

    number = input("Enter a number: ")
