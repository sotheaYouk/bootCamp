from operator import itemgetter

def dict_count2(my_list):
    dictionary = {}
    new_list = []
    total = 0
    to_return = ""
    
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
    to_return = str(new_list)

    if total != 0:
        temp = f"TOTAL: {total}"
        print(temp)
        to_return += "\n" + temp 
    else:
        temp = "Your string is empty."
        print(temp)
        to_return += "\n" + temp
    
    return to_return


dict_count2(["z", "z", "z", "z", "b", "b", "b", "b", "a", "a", "a", "a", "a", "a"])
