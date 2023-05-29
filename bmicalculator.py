from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("BMI Calculator")
root.geometry("900x600")
root.resizable(0,0)

# Function to calculate BMI
def bmicalculate():
    bmi = int(weight_entry.get())/(int(height_entry.get())/100)**2 
    bmi_label = Label(root,text=round(bmi,2))
    bmi_label.grid()

# Function to clear entry boxes.
def weight_click(event):
    weight_entry.configure()
    weight_entry.delete(0,END)
    weight_entry.unbind('<Button-1>',weight_clicked)

def height_click(event):
    height_entry.configure()
    height_entry.delete(0,END)
    height_entry.unbind('<Button-1>',height_clicked)

#FRAMES FOR THE BMI CALCULATOR
logoframe = LabelFrame(root,padx=200)
logoframe.grid(row=0,column=5)
frame_weight = LabelFrame(root,text="Weight(in kg)",font=("Helvetica",15,"bold"))
frame_weight.grid(row=0,column=10)
frame_height = LabelFrame(root,text="Height(in cm)",font=("Helvetica",15,"bold"))
frame_height.grid(row=1,column=10)

#ENTRY BOXES
weight_entry = Entry(frame_weight)
weight_entry.insert(INSERT,"Enter weight(in kg)")
weight_entry.grid(row=0,column=1)

height_entry = Entry(frame_height)
height_entry.insert(INSERT,"Enter height(in cm)")
height_entry.grid(row=1,column=1)

# When Weight entry box is clicked
weight_clicked = weight_entry.bind('<Button-1>',weight_click)

# When Height Entry Box is clicked
height_clicked = height_entry.bind('<Button-1>',height_click)

#BMI Button
calculate = Button(text="Calculate BMI",font=("Helvetica",15,"bold"),command=bmicalculate)
calculate.grid(row=2,column=10)

root.mainloop()



