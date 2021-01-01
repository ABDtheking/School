string = input("please enter a string: ")
print(string[0:len(string)//2].lower()+string[len(string)//2:].upper())