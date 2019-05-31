def acronym(my_list):

    # check empty list
    if len(my_list) == 0:
        return []
    
    else:
        
        for index in range(len(my_list)):
            temp = my_list[index].upper()
            temp = temp[0]
            my_list[index] = temp
        
        print(my_list)

        return my_list
            
        

acronym(["world", "wide", "web"])