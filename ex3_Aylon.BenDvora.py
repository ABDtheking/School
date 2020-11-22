# Aylon Ben Dvora class 8a
print ("Aylon Ben Dvora")


# ex1
print ("ex1 \nwith elif")

# ask the user for an input of a year variable
year_elif = int(input("Please enter a year: "))

# if the year is a leap year the system prints that it is a leap year
if (year_elif % 4 == 0 and year_elif % 100 != 0):
    print (f"{year_elif} is a leap year")
elif (year_elif % 400 == 0):
    print (f"{year_elif} is a leap year")

# if not the system prints it dose not a leap year
else:
    print (f"{year_elif} isn't a leap year")

print ("ex1 \nwithout elif")

# ask the user for an input of a year variable
year_noElif = int(input("Please enter a year: "))

# if the year is a leap year the system prints that it is a leap year
if ((year_noElif % 4 == 0 and year_noElif % 100 != 0) or (year_noElif % 400 == 0)):
    print (f"{year_noElif} is a leap year")

# if not the system prints it dose not a leap year
else:
    print (f"{year_noElif} isn't a leap year")


"""
used inputs ex1 (both)
1900
2000
2100
2016
1998
3456
2333
"""
# ex2
print ("ex2")
# ask the user for his age
age = int(input("Please enter your year of birth: "))
age = 2020 - age
# if his age is below 120 and grader then 18 the system prints out that he can vote for the kneset
# and if his age is below 120 and below 18 the the system prints out how much more years he need to wait before he can vote
if age >= 120:
    print ("Your age is above 120 ?!?!?!")
elif age >= 18:
    print (f"Your age is {age} , Oh your age is above 18 you can vote for the kneset")
else:
    print (f"Your age is {age}, unfortunately You need", (age-18)*(-1),"more years to vote for the kneset")
"""
used inputs ex2
1900
1990
2007
1996
"""

# ex3

# ask the user for the number of times he want to go to the pool this year
entryNum = int(input("Please enter the number of time you want to go to the pool this year: "))

# the system prints out what subscription is better for the user
if (200 + 45 * entryNum) < (400 + 30 * entryNum):
    print ("The best subscription for you is The first subscription")
else:
    print ("The best subscription for you is The second subscription")

"""
used inputs ex3
1
13
14
18
19
6
11
"""
# ex4
print ("ex4")
name = ""
NumStudentGradeAbove95 = 0
# starting a loop
while name != "FINISH":
    # asking the user for a name input
    name = input("Please enter a name: ")
    if name != "FINISH": # if name is not FINISH the system asks for a grade input
        grade = int(input("Please enter the grade: "))
        print (f"the name is {name} and the grade is {grade}") # system prints out the name and the grade
        if grade >= 95:
            NumStudentGradeAbove95 = NumStudentGradeAbove95 + 1
print (NumStudentGradeAbove95, "students grade is above 95") # system prints out the number of students that their grade is above 95 
"""
used inputs ex4
a - 12
b - 95
c - 90
d - 100
h - 98
FINISH

a - 95 
b - 85
c - 90
d - 99
h - 100
"""
# ex5
print ("ex5")
factOfNum = 1
# system asks for a number to do for him factorial
numForFact = int(input("Please enter a number that u want to calculate factorial for: "))
# in the loop system is calculating the factorial
while numForFact != 0:
    factOfNum = numForFact * factOfNum
    numForFact = numForFact - 1
print(factOfNum) # system prints the factorial for the number
"""
used inputs ex5
0
4
6
12
5
16
"""
#ex6
print("ex6")
# setting def vars
PNum = 1
NumOfNum = 0
totalNum = 0
# while the numbers are positive whe loop goes on
while PNum > 0:
    PNum = float(input("Please enter a number: "))
    # if the number is a positive number its adding him into the total and 1 to the count of nums
    if PNum > 0:
        NumOfNum = NumOfNum + 1
        totalNum = totalNum + PNum
# calculating and printing the average and the number of nums inputted
print (f"The number of numbers you entered are {NumOfNum} and the average of the numbers is",totalNum/NumOfNum)
"""
used inputs ex6
1
4
6
-2

1
5
7
2
56
8
0
"""