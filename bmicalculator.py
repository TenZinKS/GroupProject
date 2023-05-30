from tkinter import *

root=Tk()
root.title("BMI Calculator")
root.geometry("900x500")
root.resizable(0,0)

bg=PhotoImage(file="gradient.png")
bg_label=Label(root,image=bg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)


# Function to calculate BMI
def bmicalculate():
    bmi=int(weight_entry.get())/(int(height_entry.get())/100)**2
    bmi_label=Label(frame_wtht,text=round(bmi,2), bg="white", fg="black", font="bold")
    bmi_label.grid(row=1, column= 11)

# Function to clear entry boxes.
def weight_click(event):
    weight_entry.configure()
    weight_entry.delete(0,END)
    weight_entry.unbind('<Button-1>',weight_clicked)


def height_click(event):
    height_entry.configure()
    height_entry.delete(0,END)
    height_entry.unbind('<Button-1>',height_clicked)

# Function to go back to Homepage.

def back():
    root.destroy()
    import Homepage as home

# FRAMES FOR THE BMI CALCULATOR
title_frame=Frame(root, bg="white")
title_frame.pack()
# logo_frame=LabelFrame(root,padx=200)
# logo_frame.pack(side="ne")
frame_wtht=Frame(root,bg="white")
frame_wtht.place(x=90,y=80)

# TEXT / QUESTIONS
title = Label(title_frame, text="BMI CALCULATOR", font=("Lexend", 20, "bold", "underline"), bg="white", fg="black")
title.pack(padx=10, pady=5)
ask_weight=Label(frame_wtht,text="Enter your weight(in kg): ",font=("bold"),bg="white",fg="black",padx=20)
ask_weight.grid(row=0, column=1, pady=70)
ask_height=Label(frame_wtht,text="Enter your height(in cm): ",font=("bold"),bg="white",fg="black",padx=20)
ask_height.grid(row=1, column=1)

# TEXT RIGHT IN FRONT OF BMI RESULT
result = Label(frame_wtht, text="BMI: ", font=("Arial", 20, "bold"), bg="white", fg="black", padx=50)
result.grid(row=1, column=10)

backtohome = Button(frame_wtht,text="Back to Home",font=("Arial", 10, "bold"),command=back)
backtohome.grid(row=3,sticky=SW)

# ENTRY BOXES
weight_entry=Entry(frame_wtht)
weight_entry.insert(INSERT, "weight")
weight_entry.grid(row=0, column=3, ipady=5 )

height_entry=Entry(frame_wtht)
height_entry.insert(INSERT, "height")
height_entry.grid(row=1, column=3, ipady=5)

# When Weight entry box is clicked
weight_clicked=weight_entry.bind('<Button-1>',weight_click)

# When Height Entry Box is clicked
height_clicked=height_entry.bind('<Button-1>',height_click)

# BMI Button
calculate=Button(frame_wtht,text="Calculate BMI",font=("Helvetica",15,"bold"),command=bmicalculate)
calculate.grid(row=3, column=3, pady=70)



root.mainloop()