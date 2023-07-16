from tkinter import *
from tkcalendar import *
from datetime import datetime,timedelta

#Window
root = Tk()
root.title("Calendar")
root.geometry('600x400')

#Frames
frame_calendar = Frame(root)
frame_menu = Frame(root)

#Placing Frames
frame_calendar.pack(side="left",fill='both',expand=True)
frame_menu.pack(side="left")


#Functions
# def grab_date():
#     my_label.config(text=cal.get_date())


#Calendar
cal = Calendar(frame_calendar,selectmode='day')
cal.pack(fill='both',expand=True)

# Functions
def setdate():

    start_date = cal.get_date()  #Taking the entry from the entrywidget
    a = datetime.strptime(start_date,'%m/%d/%y') #Converting string to date

    end_date = a + timedelta(days=5)  #Fixing the number of Period Days 
    print(end_date) 

    my_label.config(text=f"Your period end date is: {end_date.date()}") #Using date function to represent only the date


#Button
my_button = Button(root,text="Start Period",command=setdate)
my_button.pack()

#Label
my_label = Label(root,text="Sup")
my_label.pack()


root.mainloop()