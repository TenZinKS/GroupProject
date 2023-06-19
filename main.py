from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("1920x1080")
root.title("Periodसाथी")

#Frame
login_frame = Frame(root, width=2000, height=1200, bg="white", pady=200)
login_frame.pack(fill=X, expand=True, ipady=200)

bg = PhotoImage(file="logo_whitebg.png")
bg_label = Label(login_frame,image=bg, bd=0)
bg_label.pack(side="left", padx=50)

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
    global x
    global y

    if x=="Hello" and y=="123":
        print("Entering")
    else:
        print("Incorrect")
    root.destroy()
    import Homepage as homepg

# Function after signup is pressed
def signpress():
    root.destroy()
    import signup as signin


wlcm = Label(login_frame, text="WELCOME", font=("Helvetica", 50, "bold", "underline"), bg="white", fg="black")
wlcm.pack(pady=20)

# USERNAME
usrnm = Entry(login_frame, width=40, bg="white", fg="black")
usrnm.insert(INSERT, "Username")
usrnm.pack(pady=20, ipady=5)

# PASSWORD
pw = Entry(login_frame, width=40, bg="white", fg="black", show="*")
pw.insert(INSERT, "Password")
pw.pack(pady=20, ipady=5)

# LOGIN BUTTON
login_btn = Button(login_frame, width=15, text="LogIn", font=("Arial", 20, "bold"), fg="purple", command=logPress)
login_btn.pack(pady=50)

# SIGNUP BUTTON
sgnup_btn = Button(login_frame, width=15, text="SignUp", font=("Arial", 20, "bold"), fg="purple", command=signpress)
sgnup_btn.pack()

x=usrnm
y=pw

# When Username entry box is clicked
clicked=usrnm.bind('<Button-1>',click)
# When Password Entry box is clicked
clicked2=pw.bind('<Button-1>',click2)

root.mainloop()
