message = input("Enter your encrypted message: ")
message_temp = ""
if message == "":
    print("Nothing to decode.")
else:
    for char_temp in message:

        # check special symbols and numbers 
        if not (65 <= ord(char_temp) <= 90 or 97 <= ord(char_temp) <= 122):
            message_temp += char_temp

        else:    
            char_temp = ord(char_temp)
            char_temp -= 13

            # check is within English Alphabet range
            if char_temp < 65 or 90 < char_temp < 97:
                char_temp += 26

            message_temp += chr(char_temp)

print(message_temp)
