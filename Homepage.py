from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.iconbitmap("logo1.ico")
root.title("HomePage")
root.geometry("1920x1080")

#BMI Function
def bmi():
    import bmicalculator as x

#For Background
Bg = PhotoImage(file="background.png")

#Create a Label for background. We have to use place to keep it as a background.
Bg_Label = Label(root,image=Bg)
Bg_Label.place(x=0,y=0,relwidth=1,relheight=1)

# Frames for the Homepage
calendarframe= LabelFrame(root,font=("Helvetica",15,"bold"),padx=320,bd=5)
calendarframe.grid(row=0,column=0,rowspan=3)

noteframe = LabelFrame(root,font=("Helvetica",15,"bold"),bd=5)
noteframe.grid(row=0,column=1,rowspan=3)

logoframe = LabelFrame(root,padx=5)
logoframe.grid(row=0,column=2,sticky=NE)

menuframe= LabelFrame(root,padx=100,bd=5)
menuframe.grid(row=1,column=2,sticky=E)

sloganframe = LabelFrame(root)
sloganframe.grid(row=2,column=2,sticky=SE)


# For the Calendar Frame
title = Label(calendarframe,text="Calendar",font=("Helvetica",20,"bold"))
title.grid(row=0,column=0)


# For the logo Frame
logo_img = Image.open("logo.png")
resized = logo_img.resize((200,200),Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(logoframe,image=new_logo)
logo_label.pack()

# For the Note Frame
title = Label(noteframe,text="Note",font=("Helvetica",30,"bold"),pady=10)
title.grid(row=0,column=0)
#-------------------------------------------------------------------------------------------------

spotting = Label(noteframe,text="Spotting",font=("Helvetica",10,"bold"))
spotting.grid(row=1,column=0)

clickspotting = StringVar()
clickspotting.set("Not Selected")

dropspotting = OptionMenu(noteframe,clickspotting,"NotSelected","Light","Medium","Heavy")
dropspotting.grid(row=2,column=0)
#-------------------------------------------------------------------------------------------------
clickfluid = StringVar()
clickfluid.set("Not Selected")

fluid = Label(noteframe,text="Fluid",font=("Helvetica",10,"bold"))
fluid.grid(row=3,column=0)

dropfluid = OptionMenu(noteframe,clickfluid,"NotSelected","Light","Medium","Heavy")
dropfluid.grid(row=4,column=0)

#-------------------------------------------------------------------------------------------------
clicksex = StringVar()
clicksex.set("Not Selected")

sex = Label(noteframe,text="Sex",font=("Helvetica",10,"bold"))
sex.grid(row=5,column=0)

dropsex = OptionMenu(noteframe,clicksex,"NotSelected","Light","Medium","Heavy")
dropsex.grid(row=6,column=0)

#-------------------------------------------------------------------------------------------------
clicktemp = StringVar()
clicktemp.set("Not Selected")

temperature = Label(noteframe,text="Temperature",font=("Helvetica",10,"bold"))
temperature.grid(row=7,column=0)

droptemp = OptionMenu(noteframe,clicktemp,"NotSelected","Light","Medium","Heavy")
droptemp.grid(row=8,column=0)

#---------------------------------------------------------------------------------------------
clickpain = StringVar()
clickpain.set("Not Selected")

pain = Label(noteframe,text="Pain",font=("Helvetica",10,"bold"))
pain.grid(row=9,column=0)

droppain = OptionMenu(noteframe,clickpain,"NotSelected","Light","Medium","Heavy")
droppain.grid(row=10,column=0)
#-----------------------------------------------------------------------------------------------

clickpill = StringVar()
clickpill.set("Not Selected")

pill = Label(noteframe,text="Pill",font=("Helvetica",10,"bold"))
pill.grid(row=11,column=0)

droppill = OptionMenu(noteframe,clickpill,"NotSelected","Light","Medium","Heavy")
droppill.grid(row=12,column=0)

#------------------------------------------------------------------------------------------------

clickmood = StringVar()
clickmood.set("Not Selected")

mood = Label(noteframe,text="Mood",font=("Helvetica",10,"bold"))
mood.grid(row=13,column=0)

dropmood = OptionMenu(noteframe,clickmood,"NotSelected","Light","Medium","Heavy")
dropmood.grid(row=14,column=0)
#------------------------------------------------------------------------------------------------

clickflow = StringVar()
clickflow.set("Not Selected")

flow = Label(noteframe,text="Flow",font=("Helvetica",10,"bold"))
flow.grid(row=15,column=0)

dropflow = OptionMenu(noteframe,clickmood,"NotSelected","Light","Medium","Heavy")
dropflow.grid(row=16,column=0)

#------------------------------------------------------------------------------------------------

note = Label(noteframe,text="To Note",font=("Helvetica",10,"bold"))
note.grid(row=17,column=0)

note_entry = Text(noteframe,height=18,width=50)
note_entry.grid(row=18,column=0)



# For the MenuFrame
menu_title = Label(menuframe,text="Menu",font=("Helvetica",10,"bold"))
menu_title.pack()

bmicalc = Button(menuframe,text="BMI Calculator",command = bmi)
bmicalc.pack()

workout = Button(menuframe,text="WorkOut")
workout.pack()

doanddont = Button(menuframe,text="Do's & Dont's")
doanddont.pack()

help = Button(menuframe,text="Help & Support")
help.pack()

#------------------------------------------------------------------------------------------------

#For the Slogan Frame

slogan = Label(text="Slogan")
slogan.grid(row=2,column=2)

slogan_img = Image.open("slogan.png")

resized = slogan_img.resize((250,200),Image.ANTIALIAS)

new_slogan = ImageTk.PhotoImage(resized)

slogan_label = Label(slogan,image=new_slogan)
slogan_label.pack()


root.mainloop()

