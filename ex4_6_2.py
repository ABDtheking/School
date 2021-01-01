def format_list(my_list):
    string = ""
    print(str(my_list[:-1:2]).replace("[","").replace("]",""),"and",my_list[-1])
format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"])

def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    print(list_x)
extend_list_x([4,5,6],[1,2,3])