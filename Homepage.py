from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.iconbitmap("logo1.ico")
root.title("Frames")
root.geometry("1920x1080")

#BMI Function
def bmi():
    import bmicalculator.py as bmi


#For Background
Bg = PhotoImage(file="background.png")

#Create a Label for background. We have to use place to keep it as a background.
Bg_Label = Label(root,image=Bg)
Bg_Label.place(x=0,y=0,relwidth=1,relheight=1)

# Frames for the Homepage
calendarframe= LabelFrame(root,font=("Helvetica",15,"bold"),padx=400)
calendarframe.grid(row=0,column=0)

noteframe = LabelFrame(root,font=("Helvetica",15,"bold"),padx=200)
noteframe.grid(row=0,column=1)

logoframe = LabelFrame(root,padx=100)
logoframe.grid(row=0,column=2)

menuframe= LabelFrame(root,text="Menu",padx=100)
menuframe.grid(row=1,column=2)

sloganframe = LabelFrame(root,padx=100)
sloganframe.grid(row=2,column=1)

slogan = Label(text="Slogan")
slogan.grid(row=3,column=2)


# Buttons for different frames

B1 = Button(logoframe,text ="LOGO")
B1.pack()

B1 = Button(calendarframe,text="Calendar")
B1.pack()

# For the Note Frame
spotting = Label(noteframe,text="Spotting")
spotting.grid(row=0,column=0)




# For the MenuFrame
bmicalc = Button(menuframe,text="BMI Calculator",command = bmi)
bmicalc.pack()

workout = Button(menuframe,text="WorkOut")
workout.pack()

doanddont = Button(menuframe,text="Do's & Dont's")
doanddont.pack()

help = Button(menuframe,text="Help & Support")
help.pack()


#For the Slogan

slogan_img = Image.open("slogan.png")

resized = slogan_img.resize((250,200),Image.ANTIALIAS)

new_slogan = ImageTk.PhotoImage(resized)

slogan_label = Label(slogan,image=new_slogan)
slogan_label.pack()


root.mainloop()

