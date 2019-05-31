def list_set(my_list):
    my_list = set(my_list)
    my_list = list(my_list)
    print(my_list)
    return my_list


list_set(['456', '123', '789', '123', 'abc', 'abc', 'def'])
