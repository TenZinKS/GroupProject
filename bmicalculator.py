from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Periodसाथी: BMI Calculator")
root.configure(bg='white')
root.geometry('500x550')
root.resizable(False, False)

title = Label(root, text="BMI Calculator", font=("Helvetica", 40,"bold"), background="pink", foreground="black")
title.pack(side='top', fill=X, ipady=10)
# Function to clear entry boxes.
def clear():
    weight_entry.delete(0,END)
    height_entry.delete(0,END)


# Function to calculate BMI
def bmicalculate():
    bmi=int(weight_entry.get())/(int(height_entry.get())/100)**2
    result = Label(frame, text=round(bmi,2))
    result.configure(bg='white', fg='black', font=("Arial",18,"bold"))
    result.grid(row=3, column=1)


# Creating Frame
frame =Frame(root)
frame.configure(bg='white')
frame.pack()

# Text to enter weight and height
enterweight = Label(frame, text="Enter your weight(in kg):")
enterweight.configure(fg='black', bg='white', font=('Arial'))
enterweight.grid(row=0, column=0, pady=30)

enterheight = Label(frame, text="Enter your height(in cm):")
enterheight.configure(fg='black', bg='white', font=('Arial'))
enterheight.grid(row=1, column=0)

# Entryboxes for weight and height
weight_entry = Entry(frame)
weight_entry.grid(row=0, column=1)

height_entry = Entry(frame)
height_entry.grid(row=1, column=1)

# Button to clear everything
clear_btn = Button(frame, text="Clear", command=clear)
clear_btn.configure(bg='white', height=2, width=5, bd=0)
clear_btn.grid(row=2, column=0, pady=20)

# Button that calculates BMI
calc_btn = Button(frame, text="Calculate", command=bmicalculate)
calc_btn.configure(bg='white', height=2, width=5, bd=0)
calc_btn.grid(row=2, column=1, pady=20)

# Your BMI Label
result_label = Label(frame,text='Your BMI: ')
result_label.configure(bg='white', fg='black', font=("Arial", 18, "bold"))
result_label.grid(row=3, column=0)

pic_img = Image.open("bmi_table.png")
resized = pic_img.resize((300, 250),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(root,image=new_logo, bd=0)
logo_label.pack(side='bottom')

root.mainloop()
