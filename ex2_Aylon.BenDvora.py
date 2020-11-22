
#Aylon Ben Dvora class: 8a

# ex 1
# user inputs a String
String = input("please enter a text: ")
# System is printing out the String and his length 
print(f"{String} string length is" , len(String))

# ex 2
# user inputs a String 
String2 = input("please enter a text: ")
# System print out the length of the String without spaces
print(len(String2.replace(" ","")))

# ex 3
# User inputs the String and the other vars
String3 = input("please enter a text: ")
Start = int(input("please enter the staring print point: "))
end = int(input("please enter the ending print point: "))
repeat = int(input("please enter the times you want to repeat the printing: "))
# System prints out a part of the String in new lines 
print((String3[Start:end]+"\n")*(repeat - 1)+ String3[Start:end])

# ex 4
# User inputs a string that starts with a number
String4 = input("please enter a string that starts with a number: ")
int1 = int(String4[0])
# System prints out the string with a * after it
print(String4[1:]+"*"*(int1 - len(String4[1:])))

# ex 5 
# User inputs his first and last name 
privateName = input("please enter your first name: ")
FamilyName = input("please enter your last name: ")
# if the first name and the last name starts with the same letter then it prints the name in a single line else it prints it in 2 lines
if (privateName[0] == FamilyName[0] or privateName[0] == FamilyName[0].capitalize() or privateName[0] == FamilyName[0].lower()):
    print(privateName,FamilyName)
else:
    print(privateName + "\n" + FamilyName)

# ex6
# User prints an int
int2 = int(input("please enter an INTEGER: "))
# System prints out if the number divisible by 2 or 3
if (int2 % 2 != 0 and int2 % 3 !=0):
    print("neither divisible by 2 nor by 3")
elif (int2 % 2 == 0):
    if (int2 % 3 == 0):
        print ("divisible by 2 and 3")
    else:
        print("divisible by 2")
elif(int2 % 3 == 0):
    print("divisible by 3")