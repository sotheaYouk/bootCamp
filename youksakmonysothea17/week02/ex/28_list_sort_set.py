def list_sort_set(my_list):
    my_list = set(my_list)
    my_list = list(my_list)
    my_list.sort()
    print(my_list)
    return my_list


list_sort_set([4, 2, 50, 49, 48, 1, 2, 3, 4, 5, 19])


