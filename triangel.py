a = float(input("Please enter the first side: "))
b = float(input("Please enter the second side: "))
c = float(input("Please enter the third side: "))

if (not (a + b > c and b + c > a and a + c > b)):
    print(" זה משולש שונה צלעות")
    print ("זה לא משולש")
elif (a == b == c or c == b):
        print("המשולש הוא שווה צלעות")
elif (a == b or a == c or c == b):
        print("המשולש שווה שוקיים")
else:
    print ("זה לא משולש")
