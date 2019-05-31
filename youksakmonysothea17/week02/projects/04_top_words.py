from operator import itemgetter

# return list based on the number of elements of the list
def return_list(new_list, my_list, length):
    if length >= 3:
        for index in range(length - 3, length):
            new_list.append(my_list[index][0])
        
    elif length == 2:
        for index in range(length - 2, length):
            new_list.append(my_list[index][0])
    
    elif length == 1: 
        new_list.append(my_list[length - 1][0])
    
    else: 
        return []


# count occurences of the elements in the dictionary
def count_occurrence(text, dictionary):
    for index in text:

        if index not in dictionary:
            dictionary[index] = 1

        else: 
            dictionary[index] = dictionary[index] + 1

# to remove special characters except ' 
def remove__char(text):
    for char in text:
        char_ascii = ord(char)
        if not (97 <= char_ascii <= 122 or char_ascii == 39 or char_ascii == 32 or 48 <= char_ascii <= 57):
            text = text.replace(char, '')
    
    return text


def top_words(text):
    text = text.lower()
    dictionary = {}
    my_list = []
    new_list = []

    if len(text) == 0:
        return []
    
    else:

        # to remove special characters except ' 
        text = remove__char(text)

        # split string into a list of string
        text = text.split()
        
        # counting occurrence of the words
        count_occurrence(text, dictionary)
        
        # make a list from the items of the dictionary 
        for key, value in dictionary.items():  
            my_list.append((key, value))
    
        # take only the value of the tuple
        my_list = sorted(my_list, key=itemgetter(1) )

        # return list based on the number of elements of the list
        return_list(new_list, my_list, len(my_list))

        print(new_list)
        
        return new_list

top_words("Welcome to Kirirom: Kirirom Institute of Technology and Kirirom National Parc. To contact us, send a message to us!")
