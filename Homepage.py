# from tkinter import *

# root = Tk()
# root.title("HomePage")
# # root.iconbitmap()
# root.geometry("1920x1080")

# def update():
#     my_label.config(text="New Text")

# my_label = Label(root,text="Old Text",font=("Comfortaa",100))
# my_label.pack()

# my_label.after(5000,update)

# root.mainloop()

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.iconbitmap("logo1.ico")
root.title("Frames")
root.geometry("1920x1080")

#For Background
Bg = PhotoImage(file="background.png")

#Create a Label for background. We have to use place to keep it as a background.
Bg_Label = Label(root,image=Bg)
Bg_Label.place(x=0,y=0,relwidth=1,relheight=1)

# Frames for the Homepage
calendarframe= LabelFrame(root,font=("Helvetica",15,"bold"),padx=520)
calendarframe.grid(row=0,column=0)

logoframe = LabelFrame(root,padx=200)
logoframe.grid(row=0,column=1)

menuframe= LabelFrame(root,padx=200)
menuframe.grid(row=1,column=1)

sloganframe = LabelFrame(root,padx=200)
sloganframe.grid(row=2,column=1)

slogan = Label(text="Slogan")
slogan.grid(row=3,column=1)


B1 = Button(logoframe)
B1.pack()

B1 = Button(calendarframe)
B1.pack()

B2 = Button(menuframe)
B2.pack()

#For the Slogan

slogan_img = Image.open("slogan.png")

resized = slogan_img.resize((250,200),Image.ANTIALIAS)

new_slogan = ImageTk.PhotoImage(resized)

slogan_label = Label(slogan,image=new_slogan)
slogan_label.pack()


root.mainloop()

