from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Periodसाथी")

# Setting window geometry to full screen
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()     

root.geometry("%dx%d" % (width, height))

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Function to login
def goin():
    '''
    this function takes in username/ email data and functions according to the entered data
    '''

    # Getting form data
    uname=usrnm.get()
    pwd=pw.get()

    if uname=='' or pwd=='':
        messagebox.showinfo("Error", "Cannot leave blank, Try again.")
    else:
      # Opening and connecting to database
      conn = sqlite3.connect('signup.db')
      cursor = conn.execute('SELECT * from users where Email="%s" and Password="%s"'%(uname,pwd))

      # Fetching data 
      if cursor.fetchall():
       logPress()
      else:
       messagebox.showinfo("Error", "Wrong username or password\n Try again.")

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Function when Username is clicked
def click(event):
    usrnm.configure()
    usrnm.delete(0,END)
    usrnm.unbind('<Button-1>',clicked)

# Function when Password is clicked
def click2(event):
    pw.configure()
    pw.delete(0,END)
    pw.unbind('<Button-1>', clicked2)


# Function when Login is Pressed
def logPress():
    root.destroy()
    import Homepage as homepg

# Function after signup is pressed
def signpress():
    root.destroy()
    import signup as signin

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Frame
login_frame = Frame(root, width=2000, height=1200, bg="white", pady=200)
login_frame.pack(fill=X, expand=True, ipady=200)

bg = PhotoImage(file="logo_whitebg.png")
bg_label = Label(login_frame,image=bg, bd=0)
bg_label.pack(side="left", padx=50)

# --------------------------------------------------------------------------------------------------------------------------------------------------

wlcm = Label(login_frame, text="WELCOME", font=("Helvetica", 50, "bold", "underline"), bg="white", fg="black")
wlcm.pack(pady=20)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# USERNAME
usrnm = Entry(login_frame, width=40, bg="white", fg="black")
usrnm.insert(INSERT, "Username/ email")
usrnm.pack(pady=20, ipady=5)

# PASSWORD
pw = Entry(login_frame, width=40, bg="white", fg="black", show="*")
pw.insert(INSERT, "Password")
pw.pack(pady=20, ipady=5)

# --------------------------------------------------------------------------------------------------------------------------------------------------

#BUTTONS:

# LOGIN BUTTON
login_btn = Button(login_frame, width=15, text="LogIn", font=("Arial", 20, "bold"), fg="purple", command=goin)
login_btn.pack(pady=50)

# SIGNUP BUTTON
sgnup_btn = Button(login_frame, width=15, text="SignUp", font=("Arial", 20, "bold"), fg="purple", command=signpress)
sgnup_btn.pack()

# --------------------------------------------------------------------------------------------------------------------------------------------------

# When Username entry box is clicked
clicked=usrnm.bind('<Button-1>',click)
# When Password Entry box is clicked
clicked2=pw.bind('<Button-1>',click2)

root.mainloop()
