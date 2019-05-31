def vowels(my_string):
    vowel_counter = 0
    vowel = ""
    consonant = ""

    for character in my_string.lower():

        # check vowel 
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            vowel_counter += 1 
            vowel += character

        # check white space 
        elif character == ' ':
            consonant = consonant    
        
        # check append consonant
        else:
            consonant += character
            consonant = consonant.upper()
    
    #check the number of vowel   
    if vowel_counter == 0:
        print("NO VOWELS")
        return 0
    
    # print the output 
    else:
        print(f"{vowel_counter}\n{vowel}\n{consonant}")
        
        return vowel_counter 


vowels("what is that ?")