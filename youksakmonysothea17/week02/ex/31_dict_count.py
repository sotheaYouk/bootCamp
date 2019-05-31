def dict_count(my_list):
    dictionary = {}
    
    for index in my_list:

        # check if exist 
        if index not in dictionary:
            dictionary[index] = 1

        # increment value if exist 
        else: 
            dictionary[index] = dictionary[index] + 1

    print(dictionary)

    return dictionary


dict_count(["a", "a", "a", "b", "c", "d", "c", "b", "c", "d", "c", "e", "e", "e"])
