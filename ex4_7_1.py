def squared_numbers(start, stop):
    list1 = list()
    while start < stop:
        list1.append(start*start)
        start =+ 1
    print(list1)

squared_numbers(1,10)