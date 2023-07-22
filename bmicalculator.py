from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Periodसाथी: BMI Calculator")
root.configure(bg='white')

# Setting window geometry to full screen
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()     

root.geometry("%dx%d" % (width, height))


# --------------------------------------------------------------------------------------------------------------------------------------------------

# FUNCTIONS:

# Function to calculate BMI
def bmicalculate():
    bmi=int(weight_entry.get())/(int(height_entry.get())/100)**2
    bmi_label=Label(frame_wtht,text=round(bmi,2),font=('Arial', 25, 'bold'), bg="white", fg="black")
    bmi_label.grid(row=2, column= 11)

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
    import home_frontend as home


# --------------------------------------------------------------------------------------------------------------------------------------------------

# Frame for the calculator
frame_wtht=Frame(root,bg="white")
frame_wtht.pack(fill=Y, expand=True)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# UI Optimization
random = Label(frame_wtht, text="            ", bg='white',fg='white')
random.grid(row=0, column=1, pady=100)

# Weight entry label
ask_weight=Label(frame_wtht,text="Enter your weight(in kg): ",font=('Arial',15,"bold"),bg="white",fg="black",padx=20)
ask_weight.grid(row=1, column=1, pady=50,sticky='w')

# Height entry label
ask_height=Label(frame_wtht,text="Enter your height(in cm): ",font=('Arial',15,"bold"),bg="white",fg="black",padx=20)
ask_height.grid(row=3, column=1,pady=50, sticky='w')

# TEXT RIGHT IN FRONT OF BMI RESULT
result = Label(frame_wtht, text=" Your BMI: ", font=("Arial", 30, "bold"), bg="white", fg="black")
result.grid(row=2,column=3,sticky='e', padx=50)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# ENTRY BOXES
weight_entry=Entry(frame_wtht)
weight_entry.insert(INSERT, "weight")
weight_entry.grid(row=1, column=2, ipady=5, sticky='w')

height_entry=Entry(frame_wtht)
height_entry.insert(INSERT, "height")
height_entry.grid(row=3, column=2, ipady=5, sticky='w')


# --------------------------------------------------------------------------------------------------------------------------------------------------

# When Weight entry box is clicked
weight_clicked=weight_entry.bind('<Button-1>',weight_click)

# When Height Entry Box is clicked
height_clicked=height_entry.bind('<Button-1>',height_click)


# --------------------------------------------------------------------------------------------------------------------------------------------------

# BUTTONS:

# Back to home button
backtohome = Button(frame_wtht,text="Back to Home",font=("Helvetica", 15, "bold"),command=back)
backtohome.grid(row=4,column=1, sticky='w')

# BMI Button
calculate=Button(frame_wtht,text="Calculate BMI",font=("Helvetica",15,"bold"),command=bmicalculate)
calculate.grid(row=4, column=2, pady=70, sticky='w')


# --------------------------------------------------------------------------------------------------------------------------------------------------

# For the bottom slogan
pic_img = Image.open("logo_slogan.png")
resized = pic_img.resize((500, 250),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(root,image=new_logo, bd=0)
logo_label.pack(side='bottom', pady=50)

root.mainloop()
