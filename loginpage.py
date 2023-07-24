from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Periodसाथी")
root.configure(bg='white')

# Setting window geometry to full screen
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()     

root.geometry("%dx%d" % (width, height))

# ------------------------------------------------------------------------------------------------------------

# Function to hide and show password
def show():
    eyeimg.config(file='openeye.png')
    pw.config(show="")
    eyebutton.config(command=hide)

def hide():
    eyeimg.config(file='closeeye.png')
    pw.config(show='*')
    eyebutton.config(command=show)

# ------------------------------------------------------------------------------------------------------------

# Function to login
def goin():
    '''
    This function takes in username/ email data and functions according to the entered data
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

def update_pw():
    '''
    This function opens the window to update the users password when forgot password button is clicked.
    '''
    import updatepw as newpassword
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
    import home_frontend as homepg

# Function after signup is pressed
def signpress():
    root.destroy()
    import signupdb as signin

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Frame
login_frame = Frame(root, bg="white")
login_frame.pack(side='right',padx=170, pady=100)

logo = Image.open("logoo.png")
resized = logo.resize((600,600),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(root,image=new_logo, bd=0)
logo_label.pack(side='left', padx=100)

# --------------------------------------------------------------------------------------------------------------------------------------------------

wlcm = Label(login_frame, text="WELCOME", font=("Helvetica", 50, "bold"), bg="white", fg="black")
wlcm.grid(row=0,column=1, pady=70)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# USERNAME
usrnm = Entry(login_frame)
usrnm.configure(width=40, bg="white", fg="grey", font=('AppleGothic', 15), bd=0)
usrnm.insert(INSERT, "Username/ email")
usrnm.grid(row=1, column=1, pady=10, ipady=10)

# PASSWORD
pw = Entry(login_frame)
pw.configure(width=40, bg="white", fg="grey", show="*", font=('AppleGothic', 15))
pw.insert(INSERT, "Password")
pw.grid(row=2, column=1, pady=20, ipady=8)

eyeimg =  PhotoImage(file='openeye.png')
eyebutton = Button(login_frame, image=eyeimg, bd=0, bg='white',activebackground='white',cursor='hand2', command=hide)
eyebutton.grid(row=2, column=2, padx=10)

# Remember me button   
remember = Checkbutton(login_frame)
remember.configure(text='Remember Me',background='white', font=('AppleGothic', 15))
remember.grid(row=4, column=0)

# Forget Button
forgotbutton = Button(login_frame)
forgotbutton.configure(text="Forgot Password?", bd=0, bg='white',activebackground='white', cursor='hand2', font=('AppleGothic', 12, 'bold'), command=update_pw)
forgotbutton.grid(row=4, column=1, pady=15)


# --------------------------------------------------------------------------------------------------------------------------------------------------

#BUTTONS:

# LOGIN BUTTON
login_btn = Button(login_frame)
login_btn.configure(height=1,width=10, text="LogIn", font=("AppleGothic", 20, "bold"),bg='white', fg="#AE239F",bd=0, command=goin)
login_btn.grid(row=5, column=1, pady=30)

# SIGNUP BUTTON
sgnup_btn = Button(login_frame)
sgnup_btn.configure(height=1,width=10, text="SignUp", font=("AppleGothic", 20, "bold"),bg='white', fg="#AE239F",bd=0, command=signpress)
sgnup_btn.grid(row=6, column=1, pady=20)
# --------------------------------------------------------------------------------------------------------------------------------------------------

# When Username entry box is clicked
clicked=usrnm.bind('<Button-1>',click)
# When Password Entry box is clicked
clicked2=pw.bind('<Button-1>',click2)

root.mainloop()
