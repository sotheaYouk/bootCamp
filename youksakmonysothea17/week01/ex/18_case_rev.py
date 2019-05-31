str = input("Enter a string: ")
str_temp = ""
if len(str) == 0:
    print("Empty")
else:
    for x in str:
        x = ord(x)
        if x >= 65 and x <= 90:
            x += 32
        elif x >= 97 and x <= 122:
            x -= 32
        str_temp += chr(x)
print(str_temp)
