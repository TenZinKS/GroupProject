from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import time
from plyer import notification

# To create a window
root=Tk()
root.title("Create Reminder")
root.configure(bg='white')
root.resizable(0,0)
root.geometry("500x500")
root.iconbitmap("bell.ico")

def back():
    root.destroy()
    import home_frontend

def get_details():
    """
    This function takes the data from the entry boxes and sets the remainder accordingly.
    """
    get_title = set_entry.get()
    get_msg = set_alert_entry.get()
    get_time = set_time_entry.get()
    if get_title == "" or get_msg == "" or get_time =="": #Check to see if none of the entry box is empty 
        messagebox.showerror("Alert","All fields are required!") #If one of the entry is empty show a error message
    else:
        int_time = int(float(get_time))
        min_time = int_time * 60 #converting time in to minutes
        messagebox.showinfo("Notifier Set","Set Notification")
        time.sleep(min_time)

        # notiy module which takes 4 inputs title, message,app_icon,timeout
        notification.notify(
        title = get_title,
        message = get_msg,
        app_icon = "bell.ico",
        timeout=10
        )

#Function to clear the entry fields.
def delete():
    set_entry.delete(0,END)
    set_alert_entry.delete(0,END)
    set_time_entry.delete(0,END)
        

#Labels and Entryboxes
title = Label(text="Create a Reminder",font=("Helvetica", 20, "bold"), bg='white', fg='black')
title.grid(row=0,column=1,columnspan=5,ipady=20)

set = Label(root,text="Set Title of the Reminder",font=("Helvetica", 10), bg='white', fg='black')
set.grid(row=1,column=1,ipady=10)

set_entry = Entry(root)
set_entry.grid(row=1,column=2)

set_alert = Label(root,text="Set Alert Message",font=("Helvetica", 10), bg='white', fg='black')
set_alert.grid(row=2,column=1,ipady=10)

set_alert_entry = Entry(root)
set_alert_entry.grid(row=2,column=2)

set_time = Label(root,text="Set Time",font=("Helvetica", 10), bg='white', fg='black')
set_time.grid(row=3,column=1,ipady=10)

set_time_entry = Entry(root)
set_time_entry.grid(row=3,column=2)

suffix = Label(root,text="(min)", bg='white', fg='black')
suffix.grid(row=3,column=3,ipady=10)

# Buttons
create_reminder = Button(root,text="Create Reminder",command=get_details)
create_reminder.grid(row=5,column=4,padx=20)

clear = Button(root,text="Clear",command=delete)
clear.grid(row=5,column=1,columnspan=2,padx=10)

go_back = Button(text="Back",command=back)
go_back.grid(row=5,column=0,padx=10)

# For the image.
slogan_img = Image.open("logo_slogan.png")

resized = slogan_img.resize((400,200),Image.LANCZOS)

new_slogan = ImageTk.PhotoImage(resized)

slogan_label = Label(image=new_slogan, bg='white')
slogan_label.grid(row=6,columnspan=6,padx=40,pady=20)

root.mainloop()

















