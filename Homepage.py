from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.iconbitmap("logo1.ico")
root.title("HomePage")
root.geometry("1920x1080")

# BMI button Function
def bmi():
    root.destroy()
    import bmicalculator as bmi

# Do's and Dont's button Function 
def do():
    root.destroy()
    import dos_donts as do_dont

# Back to Home button in Menu
def goback():
    root.destroy()
    import main as gologin

# Frames for the Homepage
calendarframe= LabelFrame(root,font=("Helvetica",15,"bold"), padx=400, bg="white", bd=0)
calendarframe.pack(side="left")

noteframe = LabelFrame(root,font=("Helvetica",15,"bold"), padx=60, bg="white")
noteframe.pack(side="left", fill=Y)

logoframe = LabelFrame(root, pady=40, padx=40, bg="white", bd=0)
logoframe.pack()

menuframe= LabelFrame(root, pady=120, bg="white",highlightthickness=1, bd=0)
menuframe.config(highlightbackground = "black", highlightcolor= "black")
menuframe.pack()

sloganframe = LabelFrame(root, bd=5, bg="white")
sloganframe.pack(side="right")

#-------------------------------------------------------------------------------------------------

# For the Calendar Frame
title = Label(calendarframe,text="Calendar",font=("Helvetica",20,"bold"), bg="white", fg="black", pady=500)
title.pack()

# For the logo Frame
logo_img = Image.open("logo_whitebg.png")
resized = logo_img.resize((250,150),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(logoframe,image=new_logo, bd=0)
logo_label.pack()

#-------------------------------------------------------------------------------------------------

# For the Note Frame
title = Label(noteframe,text="Note",font=("Helvetica",30,"bold"),pady=10, bg="white", fg="black")
title.grid(row=0,column=0)

spotting = Label(noteframe,text="Spotting",font=("Helvetica",12,"bold"), bg="white", fg="black")
spotting.grid(row=1,column=0, pady=5)

clickspotting = StringVar()
clickspotting.set("Not Selected")

dropspotting = OptionMenu(noteframe,clickspotting,"NotSelected","Light","Medium","Heavy")
dropspotting.grid(row=2,column=0, pady=5)

#-------------------------------------------------------------------------------------------------

clickfluid = StringVar()
clickfluid.set("Not Selected")

fluid = Label(noteframe,text="Fluid",font=("Helvetica",12,"bold"), bg="white", fg="black")
fluid.grid(row=3,column=0, pady=5)

dropfluid = OptionMenu(noteframe,clickfluid,"NotSelected","Light","Medium","Heavy")
dropfluid.grid(row=4,column=0, pady=5)

#-------------------------------------------------------------------------------------------------

clicksex = StringVar()
clicksex.set("Not Selected")

sex = Label(noteframe,text="Sex",font=("Helvetica",12,"bold"), bg="white", fg="black")
sex.grid(row=5,column=0, pady=5)

dropsex = OptionMenu(noteframe,clicksex,"NotSelected","Light","Medium","Heavy")
dropsex.grid(row=6,column=0, pady=5)

#-------------------------------------------------------------------------------------------------

clicktemp = StringVar()
clicktemp.set("Not Selected")

temperature = Label(noteframe,text="Temperature",font=("Helvetica",12,"bold"), bg="white", fg="black")
temperature.grid(row=7,column=0, pady=5)

droptemp = OptionMenu(noteframe,clicktemp,"NotSelected","Light","Medium","Heavy")
droptemp.grid(row=8,column=0, pady=5)

#---------------------------------------------------------------------------------------------
clickpain = StringVar()
clickpain.set("Not Selected")

pain = Label(noteframe,text="Pain",font=("Helvetica",12,"bold"), bg="white", fg="black")
pain.grid(row=9,column=0, pady=5)

droppain = OptionMenu(noteframe,clickpain,"NotSelected","Light","Medium","Heavy")
droppain.grid(row=10,column=0, pady=5)
#-----------------------------------------------------------------------------------------------

clickpill = StringVar()
clickpill.set("Not Selected")

pill = Label(noteframe,text="Pill",font=("Helvetica",12,"bold"), bg="white", fg="black")
pill.grid(row=11,column=0, pady=5)

droppill = OptionMenu(noteframe,clickpill,"NotSelected","Light","Medium","Heavy")
droppill.grid(row=12,column=0, pady=5)

#------------------------------------------------------------------------------------------------

clickmood = StringVar()
clickmood.set("Not Selected")

mood = Label(noteframe,text="Mood",font=("Helvetica",12,"bold"), bg="white", fg="black")
mood.grid(row=13,column=0, pady=5)

dropmood = OptionMenu(noteframe,clickmood,"NotSelected","Light","Medium","Heavy")
dropmood.grid(row=14,column=0, pady=5)
#------------------------------------------------------------------------------------------------

clickflow = StringVar()
clickflow.set("Not Selected")

flow = Label(noteframe,text="Flow",font=("Helvetica",12,"bold"), bg="white", fg="black")
flow.grid(row=15,column=0, pady=5)

dropflow = OptionMenu(noteframe,clickmood,"NotSelected","Light","Medium","Heavy")
dropflow.grid(row=16,column=0, pady=5)

#------------------------------------------------------------------------------------------------

note = Label(noteframe,text="To Note:",font=("Helvetica",18,"bold"), bg="white", fg="black")
note.grid(row=17,column=0, pady=10)

note_entry = Text(noteframe,height=15,width=50, border=True, bg="white", fg="black")
note_entry.grid(row=18,column=0)

#-------------------------------------------------------------------------------------------------

# For the MenuFrame
menu_title = Label(menuframe,text="Menu",font=("Helvetica",32,"bold"),padx=245, bg="white", fg="black")
menu_title.pack(side="top",pady=10)

bmicalc = Button(menuframe,text="BMI Calculator",command = bmi, bg="white")
bmicalc.pack(pady=10)

workout = Button(menuframe,text="WorkOut", bg="white")
workout.pack(pady=10)

doanddont = Button(menuframe,text="Do's & Dont's", bg="white", command=do)
doanddont.pack(pady=10)

help = Button(menuframe,text="Help & Support", bg="white")
help.pack(pady=10)

back = Button(menuframe, text="Back to Login", command=goback, bg="white")
back.pack(pady=10)

#------------------------------------------------------------------------------------------------

#For the Slogan Frame

slogan_img = Image.open("mainslogan.png")

resized = slogan_img.resize((400,250),Image.LANCZOS)

new_slogan = ImageTk.PhotoImage(resized)

slogan_label = Label(image=new_slogan)
slogan_label.pack(side="right")


root.mainloop()

