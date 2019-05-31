def list_sort_str(my_list):
    condition = True
    index = 0

    while condition:
        if my_list[index].isdigit() is True:
            del my_list[index]
            index = 0

        elif index == len(my_list) - 1:
            condition = False

        else:
            index += 1

    my_list.sort()
    print(my_list)

    return my_list


list_sort_str(["abc", "4", "2", "3", "dza", "def"])

