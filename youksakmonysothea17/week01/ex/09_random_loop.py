import random

N = int(input("Enter a number: "))

while N > 0:
    print(random.randint(1, 100))
    N -= 1
