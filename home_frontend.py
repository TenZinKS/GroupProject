from tkinter import *
import home_backend
from PIL import ImageTk,Image
from tkcalendar import *
from datetime import datetime,timedelta
 
root = Tk()
root.iconbitmap("logo1.ico")
root.title("HomePage")
root.geometry("1920x1080")
root.config(bg="white")

# Function of Event
def get_selected_row(event):
    global selected_tuple
    index=history_list.curselection()[0] 
    #The curselection method on listbox returns a tuple containing the indices/line numbers of the selected item(s) of the listbox, starting from 0. We also have indexed to just get the first item.

    selected_tuple=history_list.get(index) 
    period_start.config(text="Period Started:"+ selected_tuple[0]) 
    clickspotting.set(selected_tuple[1])
    clickfluid.set(selected_tuple[2])
    clicksex.set(selected_tuple[3])
    clicktemp.delete(0,END)
    clicktemp.insert(END,selected_tuple[4])
    clickpain.set(selected_tuple[5])
    clickpill.set(selected_tuple[6])
    clickmood.set(selected_tuple[7])
    

#Viewing History
def view_command():
    history_list.delete(0,END)# It is needed to clear the listbox everytime the function is called.
    for row in home_backend.view():
        history_list.insert(END,row)# The new rows are inserted at the end of the list box.

def search():
    history_list.delete(0,END)# It is needed to clear the listbox everytime the function is called.
    for row in home_backend.search(cal.get_date()):
        history_list.insert(END,row)

# To insert data into the table
def insert_command():
    home_backend.insert(cal.get_date(),clickspotting.get(),clickfluid.get(),clicksex.get(),clicktemp.get(),clickpain.get(),clickpill.get(),clickmood.get())

# To delete data from the table
def delete_command():
    home_backend.delete(selected_tuple[0])

# TO update data from the table
def update_command():
    home_backend.update(selected_tuple[0],clickspotting.get(),clickfluid.get(),clicksex.get(),clicktemp.get(),clickpain.get(),clickpill.get(),clickmood.get())

#BMI Function
def bmi():
    root.destroy()
    import bmicalculator as bmi


# Function to go back to LogIn.
def back():
    root.destroy()
    import main as home


def setdate():
    start_date = cal.get_date()  #Taking the entry from the entrywidget
    date_obj = datetime.strptime(start_date, '%m/%d/%y') #Converting string into datetime object
    end_date = date_obj + timedelta(days=4)  #Fixing the number of Period Days 
    ovulation_start_date = date_obj + timedelta(days=10)
    ovulation_end_date = date_obj + timedelta(days=15)

    period_end.config(text=f"Your period end date is: {end_date.date()}") #Using date function to represent only the date.
    ovul_period.config(text=f"Your ovulation period is from: {ovulation_start_date.date()} to {ovulation_end_date.date()} ")
    
    
# Frames for the Homepage
calendarframe= LabelFrame(root,bg="white")
noteframe = LabelFrame(root,font=("Helvetica",15,"bold"))
logoframe = Frame(root,bg="white")
menuframe= LabelFrame(root,bg="white")
sloganframe = Frame(root,bg="white")

#Placement of Frames
calendarframe.pack(side="left",fill='both',expand=True)
noteframe.pack(side="left")
logoframe.pack()
menuframe.pack()
sloganframe.pack()


# For the Calendar Frame
cal = Calendar(calendarframe,selectmode='day',showweeknumbers = False,showothermonthdays=False,background="pink",foreground ="black",selectbackground = "pink",weekendbackground = "white",weekendforeground = "black")
cal.pack(fill="both",expand=True)

# To create Buttons
start_button = Button(calendarframe,text="Start Period",command=lambda:setdate())
start_button.pack(side="left",pady=10)

get_history_btn = Button(calendarframe,text="Get History",command=lambda:search())
get_history_btn.pack(side="right",anchor="center")

#Creating a label to show the period end month

period_end = Label(calendarframe,text="")
period_end.pack()
ovul_period = Label(calendarframe,text="")
ovul_period.pack()


# For the logo Frame
logo_img = Image.open("logo.png")
resized = logo_img.resize((200,200),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(logoframe,image=new_logo)
logo_label.pack(fill="both",expand=True)


# For the Note Frame
title = Label(noteframe,text="Note",font=("Helvetica",20,"bold"),pady=10)
period_start = Label(noteframe,text="")


spotting = Label(noteframe,text="Spotting",font=("Helvetica",10,"bold"))
spotting_options = ["NotSelected","Light","Medium","Heavy"]

clickspotting = StringVar()
clickspotting.set("Not Selected")
dropspotting = OptionMenu(noteframe,clickspotting,*spotting_options)

fluid = Label(noteframe,text="Fluid",font=("Helvetica",10,"bold"))
fluid_options = ["NotSelected","Egg-white","Absent","Creamy","Atypical"]

clickfluid = StringVar()
clickfluid.set("Not Selected")
dropfluid = OptionMenu(noteframe,clickfluid,*fluid_options)

sex = Label(noteframe,text="Sex",font=("Helvetica",10,"bold"))
sex_options = ["NotSelected","Unprotected","Protected","Withdrawal"]

clicksex = StringVar()
clicksex.set("Not Selected")
dropsex = OptionMenu(noteframe,clicksex,*sex_options)

temperature = Label(noteframe,text="Temperature(°C)",font=("Helvetica",10,"bold"))
clicktemp = Entry(noteframe)

pain = Label(noteframe,text="Pain",font=("Helvetica",10,"bold"))
pain_options = ["NotSelected","Cramps","Headaches","Tender Breasts"]
clickpain = StringVar()
clickpain.set("Not Selected")
droppain = OptionMenu(noteframe,clickpain,*pain_options)

pill = Label(noteframe,text="Pill",font=("Helvetica",10,"bold"))
pill_options = ["NotSelected","Taken","Missed","Late","Double"]

clickpill = StringVar()
clickpill.set("Not Selected")
droppill = OptionMenu(noteframe,clickpill,*pill_options)

mood = Label(noteframe,text="Mood",font=("Helvetica",10,"bold"))
mood_options = ["NotSelected","Happy","Sensitive","Sad","PMS"]

clickmood = StringVar()
clickmood.set("Not Selected")
dropmood = OptionMenu(noteframe,clickmood,*mood_options)
#---------------------------------------------------------------------------

#Label Placement
title.pack()
period_start.pack()
spotting.pack()
dropspotting.pack()
fluid.pack()
dropfluid.pack()
sex.pack()
dropsex.pack()
temperature.pack()
clicktemp.pack()
pain.pack()
droppain.pack()
pill.pack()
droppill.pack()
mood.pack()
dropmood.pack()


# ------------------------------------------------------------

save = Button(noteframe,text="Save",font=("Helvetica",10,"bold"),command = insert_command)
save.pack()

history = Label(noteframe,text="History",font=("Helvetica",20,"bold"))
history.pack()

history_list = Listbox(noteframe,height=18,width=50)
history_list.pack()

history_list.bind('<<ListboxSelect>>',get_selected_row)

view = Button(noteframe,text="View History",font=("Helvetica",10,"bold"),command = view_command)
view.pack(side="left")

delete_btn = Button(noteframe,text="Delete Selected",font=("Helvetica",10,"bold"),command = delete_command)
delete_btn.pack(side="left")


update_btn = Button(noteframe,text="Update Selected",font=("Helvetica",10,"bold"),command = update_command)
update_btn.pack(side="left")

#-------------------------------------------------------------------------------------

# For the MenuFrame

bmicalc = Button(menuframe,text="BMI Calculator",command = bmi)
workout = Button(menuframe,text="WorkOut")
doanddont = Button(menuframe,text="Do's & Dont's")
help = Button(menuframe,text="Help & Support")

#Menu Placement

bmicalc.pack()
workout.pack()
doanddont.pack() 
help.pack()

#------------------------------------------------------------------------------------------------

# For the Slogan Frame

slogan_img = Image.open("mainslogan.png")

resized = slogan_img.resize((200,200),Image.LANCZOS)

new_slogan = ImageTk.PhotoImage(resized)

slogan_label = Label(image=new_slogan)
slogan_label.pack()


root.mainloop()

