str = input("Enter a string: ")
str_temp = ""
while str != "Generate":
    str_temp += "<p>" + str + "</p>\n"
    str = input("Enter a string: ")
print(str_temp)
