list1 = []
whilen = 0
while whilen < 100:
    int1 = int(input("Please enter a number: "))
    list1.insert(whilen,int1)
    whilen = whilen + 1
list1.sort()
print(list1)