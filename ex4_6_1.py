def shift_left(my_list):
    my_list.append(my_list[0])
    my_list.pop(0)
    print(my_list)
shift_left(['monkey', 2.0, 1])

