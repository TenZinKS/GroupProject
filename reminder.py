from tkinter import *
from tkinter import messagebox
import time
from plyer import notification

# To create a window
root=Tk()
root.title("Create Reminder")
root.resizable(0,0)
root.geometry("500x500")
root.iconbitmap("bell.ico")


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
title = Label(text="Create a Reminder",font=("Helvetica", 20, "bold"))
title.grid(row=0,column=1,columnspan=5,ipady=20)

set = Label(root,text="Set Title of the Reminder",font=("Helvetica", 10))
set.grid(row=1,column=1,ipady=10)

set_entry = Entry(root)
set_entry.grid(row=1,column=2)

set_alert = Label(root,text="Set Alert Message",font=("Helvetica", 10))
set_alert.grid(row=2,column=1,ipady=10)

set_alert_entry = Entry(root)
set_alert_entry.grid(row=2,column=2)

set_time = Label(root,text="Set Time",font=("Helvetica", 10))
set_time.grid(row=3,column=1,ipady=10)

set_time_entry = Entry(root)
set_time_entry.grid(row=3,column=2)

suffix = Label(root,text="(min)")
suffix.grid(row=3,column=3,ipady=10)

# Buttons
create_reminder = Button(root,text="Create Reminder",command=get_details)
create_reminder.grid(row=4,column=4,padx=20)

clear = Button(root,text="Clear",command=delete)
clear.grid(row=4,column=0,padx=10)



root.mainloop()

















