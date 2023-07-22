from tkinter import *
import home_backend
from PIL import ImageTk,Image
from tkcalendar import *
from datetime import datetime,timedelta

# ------------------------------------------------------------------------------------------------------------------------------

root = Tk()
root.iconbitmap("logo1.ico")
root.title("HomePage")
root.config(bg="white")

# Setting window geometry to full screen
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()     

root.geometry("%dx%d" % (width, height))


# ------------------------------------------------------------------------------------------------------------------------------

# Function of Event
def get_selected_row(event):
    global selected_tuple
    index=history_list.curselection()[0] 
    # The curselection method on listbox returns a tuple containing the indices/line numbers of the selected item(s)
    # of the listbox, starting from 0. We also have indexed to just get the first item.

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
    
# ------------------------------------------------------------------------------------------------------------------------------

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
    root.destory()
    import bmicalculator as bmi


# Function to go back to LogIn.
def back():
    root.destroy()
    import loginpage as home

def helpp():
    root.destroy()
    import help_and_support as gotohelp

def setdate():
    start_date = cal.get_date()  #Taking the entry from the entrywidget
    date_obj = datetime.strptime(start_date, '%m/%d/%y') #Converting string into datetime object
    end_date = date_obj + timedelta(days=4)  #Fixing the number of Period Days 
    ovulation_start_date = date_obj + timedelta(days=10)
    ovulation_end_date = date_obj + timedelta(days=15)

    period_end.config(text=f"Your period end date is: {end_date.date()}") #Using date function to represent only the date.
    ovul_period.config(text=f"Your ovulation period is from: {ovulation_start_date.date()} to {ovulation_end_date.date()} ")

# ------------------------------------------------------------------------------------------------------------------------------
    
# Frames for the Homepage
calendarframe= LabelFrame(root,bg="white")

noteframe = LabelFrame(root,font=("Helvetica",15,"bold"), bg="white")

logoframe = Frame(root,bg="white")

menuframe= LabelFrame(root,bg="white", bd=0)

sloganframe = Frame(root,bg="white")

#Placement of Frames
calendarframe.pack(side="left",fill='both',expand=True)
noteframe.pack(side="left", fill=Y)
logoframe.pack(ipadx=15)
menuframe.pack(ipadx=80, ipady=40)
sloganframe.pack(ipadx=20)

# ------------------------------------------------------------------------------------------------------------------------------

# For the Calendar Frame
cal = Calendar(calendarframe,selectmode='day',showweeknumbers = False,showothermonthdays=False,background="pink",foreground ="black",selectbackground = "pink",weekendbackground = "white",weekendforeground = "black")
cal.pack(fill="both",expand=True)

# To create Buttons
start_button = Button(calendarframe,text="Start Period",command=lambda:setdate())
start_button.configure(bg="white", fg="black", height=2, font=('Arial', 13, 'bold'))
start_button.pack(side="left",pady=10, padx=20)

get_history_btn = Button(calendarframe,text="Get History",command=lambda:search())
get_history_btn.configure(bg="white", fg="black", height=2, font=('Arial', 13, 'bold'))
get_history_btn.pack(side="right",anchor="center", padx=20)

# Creating a label to show the period end month
period_end = Label(calendarframe,text="", bg="white", fg="black")
period_end.pack()
ovul_period = Label(calendarframe,text="", bg="white", fg="black")
ovul_period.pack()


# ------------------------------------------------------------------------------------------------------------------------------

# For the logo Frame
logo_img = Image.open("logoo.png")
resized = logo_img.resize((200,200),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(logoframe,image=new_logo, bg="white")
logo_label.pack(fill="both",expand=True)


# ------------------------------------------------------------------------------------------------------------------------------

# For the Note Frame
title = Label(noteframe,text="Note",font=("Helvetica",20,"bold"), bg="white", fg="black",pady=10)
period_start = Label(noteframe,text="", bg='white', fg='black')

spotting = Label(noteframe,text="Spotting",font=("Helvetica",12,"bold"), bg="white", fg="black")
spotting_options = ["NotSelected","Light","Medium","Heavy"]

clickspotting = StringVar()
clickspotting.set("Not Selected")
dropspotting = OptionMenu(noteframe,clickspotting,*spotting_options)

fluid = Label(noteframe,text="Fluid",font=("Helvetica",12,"bold"), bg="white", fg="black")
fluid_options = ["NotSelected","Egg-white","Absent","Creamy","Atypical"]

clickfluid = StringVar()
clickfluid.set("Not Selected")
dropfluid = OptionMenu(noteframe,clickfluid,*fluid_options)

sex = Label(noteframe,text="Sex",font=("Helvetica",12,"bold"), bg="white", fg="black")
sex_options = ["NotSelected","Unprotected","Protected","Withdrawal"]

clicksex = StringVar()
clicksex.set("Not Selected")
dropsex = OptionMenu(noteframe,clicksex,*sex_options)

temperature = Label(noteframe,text="Temperature(°C)",font=("Helvetica",12,"bold"), bg="white", fg="black")
clicktemp = Entry(noteframe, bg="white", fg="black")

pain = Label(noteframe,text="Pain",font=("Helvetica",12,"bold"), bg="white", fg="black")
pain_options = ["NotSelected","Cramps","Headaches","Tender Breasts"]

clickpain = StringVar()
clickpain.set("Not Selected")
droppain = OptionMenu(noteframe,clickpain,*pain_options)

pill = Label(noteframe,text="Pill",font=("Helvetica",12,"bold"), bg="white", fg="black")
pill_options = ["NotSelected","Taken","Missed","Late","Double"]

clickpill = StringVar()
clickpill.set("Not Selected")
droppill = OptionMenu(noteframe,clickpill,*pill_options)

mood = Label(noteframe,text="Mood",font=("Helvetica",12,"bold"), bg="white", fg="black")
mood_options = ["NotSelected","Happy","Sensitive","Sad","PMS"]

clickmood = StringVar()
clickmood.set("Not Selected")
dropmood = OptionMenu(noteframe,clickmood,*mood_options)

# ------------------------------------------------------------------------------------------------------------------------------

# Label Placement
title.pack(pady=5)
period_start.pack()
spotting.pack(pady=5)
dropspotting.pack()
fluid.pack(pady=5)
dropfluid.pack()
sex.pack(pady=5)
dropsex.pack()
temperature.pack(pady=5)
clicktemp.pack()
pain.pack(pady=5)
droppain.pack()
pill.pack(pady=5)
droppill.pack()
mood.pack(pady=5)
dropmood.pack()

save = Button(noteframe,text="Save",font=("Helvetica",12,"bold"),command = insert_command, bg="white", fg="black")
save.configure(height=2, width=10)
save.pack(pady=20)

history = Label(noteframe,text="History",font=("Helvetica",20,"bold"), bg="white", fg="black")
history.pack()

history_list = Listbox(noteframe,height=18,width=50, bg="white", fg="black")
history_list.pack(pady=30)

history_list.bind('<<ListboxSelect>>',get_selected_row)

view = Button(noteframe,height=3,text="View History",font=("Helvetica",13,"bold"),command = view_command, bg="white", fg="black")
view.pack(side="left", padx=10, pady=10)

delete_btn = Button(noteframe,height=3,text="Delete Selected",font=("Helvetica",13,"bold"),command = delete_command, bg="white", fg="black")
delete_btn.pack(side="left", padx=10, pady=10)


update_btn = Button(noteframe,height=3,text="Update Selected",font=("Helvetica",13,"bold"),command = update_command, bg="white", fg="black")
update_btn.pack(side="left", padx=10, pady=10)


# ------------------------------------------------------------------------------------------------------------------------------

# For the MenuFrame

menu_txt = Label(menuframe, text="MENU", bg='white', fg='black')
menu_txt.configure(font=("Helvetica", 20, "bold"))

bmicalc = Button(menuframe,text="BMI Calculator",command = bmi)
bmicalc.configure(height=2, width=10)

workout = Button(menuframe,text="WorkOut")
workout.configure(height=2, width=10)

doanddont = Button(menuframe,text="Do's & Dont's")
doanddont.configure(height=2, width=10)

help = Button(menuframe,text="Help & Support", command=helpp)
help.configure(height=2, width=10)

gotologin = Button(menuframe, text="Login Menu", command=back)
gotologin.configure(height=2, width=10)

# Menu Placement
menu_txt.pack(pady=40)
bmicalc.pack(pady=20)
workout.pack(pady=20)
doanddont.pack(pady=20)
help.pack(pady=20)
gotologin.pack(pady=20)

# ------------------------------------------------------------------------------------------------------------------------------

# For the Slogan Frame

slogan_img = Image.open("mainslogan.png")

resized = slogan_img.resize((200,200),Image.LANCZOS)

new_slogan = ImageTk.PhotoImage(resized)

slogan_label = Label(image=new_slogan, bg='white')
slogan_label.pack(padx=40)

# ------------------------------------------------------------------------------------------------------------------------------

root.mainloop()

