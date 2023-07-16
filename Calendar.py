from tkinter import *
from tkcalendar import *
from datetime import datetime,timedelta

# Window
root = Tk()
root.geometry('380x200')


# Functions
def setdate():
    
    start_date = period_start_date.get_date()  #Taking the entry from the entrywidget
    end_date = start_date + timedelta(days=5)  #Fixing the number of Period Days 
    print(end_date) 

    end.config(text=f"Your period end date is: {end_date}") #Using date function to represent only the date


# To create dateentry
period_start_date = DateEntry(root)
period_start_date.pack()

# To create Buttons
start_button = Button(root,text="Start Period",command=lambda:setdate())
start_button.pack(pady=20)

#Creating a label to show the period end month
end = Label(text="Hello")
end.pack(pady=40)


#run
root.mainloop()






