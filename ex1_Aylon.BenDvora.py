#Aylon Ben Dvora class: 8a

#ex 1
#setting variables
one_str = "one"
one_float = 1.0
one_int = 1 

#printing the type of the variables 
print(type(one_float),type(one_int),type(one_str))

#changeing all variables types to string 
one_float = str(one_float)
one_int = str(one_int)

#printing one=1=1.0
print(one_str+"="+one_int+"="+one_float)

#printing one= 1= 1.0
print(one_str+"= "+one_int+"= "+one_float)


#ex 2 
#user inputs the leg numbers
leg_1 = float(input("please enter first leg: "))
leg_2 = float(input("plz enter second leg: "))

#calculating the hypotenuse and the area
hypotenuse = (leg_1**2 + leg_2**2) ** 0.5
area = (leg_1*leg_2)/2

#printing the hypotenuse and the area
print("The length of the hypotenuse is: " , hypotenuse, " \nArea of the triangle is: ", area)


#ex 3
#user input the number of books
books = input("please enter number of books: ")

#calculate and prints the number of shelfs needed and the number of books in the cart
print("Number of the required shelves is:",int(books)//15,"\nNumber of books on the book cart:",int(books)%15)

#ex 4 
#user inputs a dubble-digit number
dubble_digit= str(input("please enter a dubble-digit number: "))

#printing the sum of the digits of the dubble-digit number
print("The sum of the digits of the dubble-digit number is: ",int(dubble_digit[0])+int(dubble_digit[1]))

#user inputs a tripple-digit number 
tripple_digit= str(input("please enter a tripple-digit number: "))

#printing the sum of the digits of the tripple-digit number
print("The sum of the digits of the tripple-digit number is: ",int(tripple_digit[0])+int(tripple_digit[1])+int(tripple_digit[2]))
