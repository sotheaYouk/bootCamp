import random

play = True

while play:
    count = 0
    condition = True
    random_number = random.randrange(1, 100)
    
    name = input("Hello, what is your name?\n")
    print(f"Well {name}, try to guess the number I have in mind!")
    number = int(input())

    while condition:
        count += 1
        
        if number == random_number:
            print(f"It took you {count} turns to guess my number which was {random_number}!")
            condition = False
        elif number > random_number:
            number = int(input("Too high, try again!\n"))
        else:
            number = int(input("Too low, try again!\n"))
    play_again = input("Do you want to play again? [Y/N]?\n")
    while not play_again == 'Y' or play_again == 'N':
        if play_again == 'Y':
            play = play
        elif play_again == 'N':
            print(f"Ok, bye {name}! See you later!")
            play = False
            break
        else:
            print("Sorry, I did not understand. Let me repeat:")
            play_again = input("Do you want to play again?\n")

