import tkinter as tk
import tkinter.simpledialog
import tkinter.font

# main window

main = tk.Tk()
size = tk.Canvas(main)

# exercise functions 

def showEx1():
    String = tk.simpledialog.askstring("string","Please enter a string")
    ex1w = tk.Toplevel()
    l1 = tk.Label(ex1w,text = f"{String} string length is" + " " + str(len(String)))
    l1.pack()

def showEx2():
    String = tk.simpledialog.askstring("String","Please enter a string")
    ex2w = tk.Toplevel()
    l1 = tk.Label(ex2w,text = str(len(String.replace(" ",""))))
    l1.pack()

def showEx3():
    StringIn = tk.simpledialog.askstring("Your String","Please enter a string")
    Start = tk.simpledialog.askinteger("start","Enter a starting print point")
    end = tk.simpledialog.askinteger("End","Please enter ending print point")
    repeat = tk.simpledialog.askinteger("repeat","Please enter the times you want to repeat printing")
    String = str(StringIn)
    ex3w = tk.Toplevel()
    l1 = tk.Label(ex3w,text = (String[Start:end]+"\n")*(repeat - 1)+ String[Start:end])
    l1.pack()

def showEx4():
    nums = tk.simpledialog.askstring("nums","Please enter a string that starts with a number")
    int1 = int(nums[0])
    ex4w = tk.Toplevel()
    l1 = tk.Label(ex4w,text = nums[1:]+"*"*(int1 - len(nums[1:])))
    l1.pack()

def showEx5():
    firstName = tk.simpledialog.askstring("fName","Please enter your first name")
    lastName = tk.simpledialog.askstring("lName","please enter your last name")
    ex5w = tk.Toplevel()
    if (firstName[0] == lastName[0] or firstName[0] == lastName[0].capitalize() or firstName[0] == lastName[0].lower()):
        l1 = tk.Label(ex5w,text = (firstName,lastName))
        l1.pack()
    else:
        l1 = tk.Label(ex5w,text = (firstName + "\n" + lastName))
        l1.pack()

def showEx6():
    int2 = tk.simpledialog.askinteger("int","Please enter an INTEGER")
    ex6w = tk.Toplevel()
    if (int2 % 2 != 0 and int2 % 3 !=0):
        l1 = tk.Label(ex6w,text ="neither divisible by 2 nor by 3")
        l1.pack()
    elif (int2 % 2 == 0):
        if (int2 % 3 == 0):
            l1 = tk.Label(ex6w,text = "divisible by 2 and 3")
            l1.pack()
        else:
            l1 = tk.Label(ex6w, text = "divisible by 2")
            l1.pack()
    elif(int2 % 3 == 0):
        l1 = tk.Label(ex6w, text = "divisible by 3")
        l1.pack()

# exercises buttons 

Font = tk.font.Font(size = 50)
bex1 = tk.Button(size,text = "Exercise 1",command = showEx1,font = Font)
bex1.pack()
bex2 = tk.Button(size,text = "Exercise 2",command = showEx2,font = Font)
bex2.pack()
bex3 = tk.Button(size,text = "Exercise 3",command = showEx3,font = Font)
bex3.pack()
bex4 = tk.Button(size,text = "Exercise 4",command = showEx4,font = Font)
bex4.pack()
bex5 = tk.Button(size,text = "Exercise 5",command = showEx5,font = Font)
bex5.pack()
bex6 = tk.Button(size,text = "Exercise 6",command = showEx6,font = Font)
bex6.pack()

size.pack()
main.mainloop()