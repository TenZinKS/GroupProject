from tkinter import *

#window
root = Tk()
root.title("Calculator")
root.resizable(0,0)

# Creating a Frame Showing all operations up until now.
Process = Frame(root,bd =5)
Process.grid()

calculation = Label(Process)
calculation.grid()

#Functions
def click(num):
    digit = display.get()
    display.delete(0,END)
    display.insert(0, str(digit) + str(num))

def sum():
    global first_num
    global operation
    global prev_num
    operation = "Addition"
    first_num = int(display.get())
    calculation.config(text=str(display.get()) + " + ")
    prev_num = str(first_num) + " + "
    display.delete(0,END)


def diff():
    global first_num
    global operation
    global prev_num
    operation = "Subtraction"
    first_num = int(display.get())
    calculation.config(text=str(display.get()) + " - ")
    prev_num = str(first_num) + " - "
    display.delete(0,END)

def pro():
    global first_num
    global operation
    global prev_num
    operation = "Multiplication"
    first_num = int(display.get())
    calculation.config(text=str(display.get()) + " X ")
    prev_num = str(first_num) + " X "
    display.delete(0,END)

def div():
    global first_num
    global operation
    global prev_num
    operation = "Divison"
    first_num = int(display.get())
    calculation.config(text=str(display.get()) + " / ")
    prev_num = str(first_num) + " / "
    display.delete(0,END)

def mod():
    global first_num
    global operation
    global prev_num
    operation = "MOD"
    first_num = int(display.get())
    calculation.config(text=str(display.get()) + " MOD ")
    prev_num = str(first_num) + " MOD "
    display.delete(0,END)

def output():
    global second_num
    second_num = int(display.get())
    display.delete(0,END)
    if operation == "Addition":
        calculation.config(text=prev_num + str(second_num))
        display.insert(0, first_num + second_num)
    elif operation == "Subtraction":
        calculation.config(text=prev_num + str(second_num))
        display.insert(0, first_num - second_num)
    elif operation == "Multiplication":
        calculation.config(text=prev_num + str(second_num))
        display.insert(0, first_num * second_num)
    elif operation == "Divison":
        calculation.config(text=prev_num + str(second_num))
        try: #For Zero Division Error
            display.insert(0, first_num / second_num)
        except Exception:
            display.insert(0,"ERROR")
    elif operation == "MOD":
        calculation.config(text=prev_num + str(second_num))
        display.insert(0, first_num % second_num)

def clear():
    calculation.config(text="")
    display.delete(0,END)

def quit():
    root.quit()

#Display Widget
display = Entry(root,width=80,bd=5)
display.grid(row=1,column=0,columnspan=4,padx=10,pady=10,ipady=5)

#NUMBER Buttons
num1 = Button(text="1",font=20,padx=50,pady=30,command=lambda: click(1))
num2 = Button(text="2",font=20,padx=50,pady=30,command=lambda: click(2))
num3 = Button(text="3",font=20,padx=50,pady=30,command=lambda: click(3))
num4 = Button(text="4",font=20,padx=50,pady=30,command=lambda: click(4))
num5 = Button(text="5",font=20,padx=50,pady=30,command=lambda: click(5))
num6 = Button(text="6",font=20,padx=50,pady=30,command=lambda: click(6))
num7 = Button(text="7",font=20,padx=50,pady=30,command=lambda: click(7))
num8 = Button(text="8",font=20,padx=50,pady=30,command=lambda: click(8))
num9 = Button(text="9",font=20,padx=50,pady=30,command=lambda: click(9))
num0 = Button(text="0",font=20,padx=50,pady=30,command=lambda: click(0))
num00 = Button(text="00",font=20,padx=45,pady=30,command=lambda: click("00"))

#Arithmetic Buttons
equal = Button(text="=",font=20,padx=111,pady=30,command=output)
add = Button(text="+",font=20,padx=47,pady=30,command=sum)
mul = Button(text="X",font=20,padx=47,pady=30,command=pro)
subtract = Button(text="-",font=20,padx=50,pady=30,command=diff)
exit = Button(text="Exit",font=20,padx=37,pady=30,command=quit)
clr = Button(text="C",font=20,padx=49,pady=30,command=clear)
mod_divide = Button(text="Mod",font=20,padx=36,pady=30,command=mod)
divide = Button(text="/",font=20,padx=52,pady=30,command=div)

# Number Button Placement
num1.grid(row=5,column=0)
num2.grid(row=5,column=1)
num3.grid(row=5,column=2)
num4.grid(row=4,column=0)
num5.grid(row=4,column=1)
num6.grid(row=4,column=2)
num7.grid(row=3,column=0)
num8.grid(row=3,column=1)
num9.grid(row=3,column=2)
num0.grid(row=6,column=0)
num00.grid(row=6,column=1)

# Arithmetic Button Placement
equal.grid(row=6,column=2,columnspan=2)
add.grid(row=2,column=3)
subtract.grid(row=4,column=3)
mul.grid(row=3,column=3)
exit.grid(row=5,column=3)
clr.grid(row=2,column=0)
mod_divide.grid(row=2,column=1)
divide.grid(row=2,column=2)


root.mainloop()