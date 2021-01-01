num1 = 20.5
num2 = 7
if num1>num2:
    if num1%num2 == 0:
        num1 = num1 + 4
    else:
        num2 = num2 + 2
        num1 = num1 - 1
elif num1 == num2:
    num2 = num2 - 3
else:
    num1 = num2 + 10
print ("num1 =",num1,"num2 =", num2)