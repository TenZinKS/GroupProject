from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("1920x1080")

bg = PhotoImage(file="theme.png")
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

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
    import Homepage as home

# Function after signup is pressed
def signpress():
    root.destroy()
    import signup as signin

login_frame = Frame(root, width=500, height=500, bg="white")
login_frame.place(x=750, y=200)

wlcm = Label(login_frame, text="WELCOME", font=("Comic Sans MS", 30, "bold", "underline"), bg="white", fg="black")
wlcm.pack(pady=20)

usrnm = Entry(login_frame, width=40, bg="white", fg="black")
usrnm.insert(INSERT, "Username")
usrnm.pack(pady=30)

pw = Entry(login_frame, width=40, bg="white", fg="black")
pw.insert(INSERT, "Password")
pw.pack()

login_btn = Button(login_frame, width=15, text="LogIn", font=("Arial", 20, "bold"), fg="purple", command=logPress)
login_btn.pack(pady=50)

sgnup_btn = Button(login_frame, width=15, text="SignUp", font=("Arial", 20, "bold"), fg="purple", command=signpress)
sgnup_btn.pack()

x=usrnm
y=pw

# When Username entry box is clicked
clicked=usrnm.bind('<Button-1>',click)
# When Password Entry box is clicked
clicked2=pw.bind('<Button-1>',click2)

root.mainloop()
