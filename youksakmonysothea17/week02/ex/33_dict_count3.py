def dict_count3(my_list):
    dictionary = {}
    new_list = []
    total = 0
    
    for index in my_list:

        # check if exist 
        if index not in dictionary:
            dictionary[index] = 1

        # increment value if exist 
        else: 
            dictionary[index] = dictionary[index] + 1

    for key, value in dictionary.items():  
        total += value
        new_list.append((key, value))
    
    new_list.sort()
    print(new_list)

    if total != 0:
        print(f"TOTAL: {total}")
        
    else:  
        print("Your string is empty.")
    
    return new_list


dict_count3(["a", "b", "b", "c", "c", "c", "c", "d", "d", "e", "e", "e"])
