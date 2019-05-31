def one_two_pair(dictionary):
    count = 0 

    for dict_values in dictionary.values():
        if dict_values == 2:
            count += 1

    if count == 1:
        print("One pair") 

    elif count == 2: 
        print("Two pair") 
    
    else:
        print("hell no")


one_two_pair({'a': 1,
                'b': 2,
                'c': 1,
                'd': 1})