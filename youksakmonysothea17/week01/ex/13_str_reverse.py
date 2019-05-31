str = input("Enter a string: ")
i = 1
str_temp = ""
while i <= len(str):
    str_temp = str_temp + str[len(str) - i]
    i += 1
print(str_temp)

