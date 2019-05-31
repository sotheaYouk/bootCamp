def list_sort_int(my_list):
    
    my_list = set(my_list)
    my_list = list(my_list)
    my_list.sort()

    condition = True
    index = 0

    while condition:

        # check if digit
        if not my_list[index].isdigit() or ord(my_list[index]) < 0:
            del my_list[index]
            index = 0

        elif index == len(my_list) - 1:
            condition = False

        else:
            index += 1

    index = 0 

    for index in range(len(my_list)):
        my_list[index] = int(my_list[index])

    print(my_list)

    return my_list


list_sort_int(["abc", "4", "4", "4", "4", "2", "3", "-9", "-10", "dza", "def"])

