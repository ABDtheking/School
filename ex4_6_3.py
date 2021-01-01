def are_lists_equal(list1, list2):
    if list1.sort() == list2.sort():
        print(True)
    else:
        print(False)


list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]

are_lists_equal(list1,list2)

are_lists_equal(list1,list3)

def longest(my_list):
    my_list = sorted(my_list,key = len)
    print(my_list[-1])




list1 = ["111", "234", "2000", "goru", "birthday", "09"]
longest(list1)