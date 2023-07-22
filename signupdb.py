from tkinter import*
from PIL import ImageTk,Image
from tkcalendar import DateEntry
import sqlite3

root = Tk()
root.title("SignUp")

# Setting window geometry to full screen
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()     

root.geometry("%dx%d" % (width, height))

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Connecting database and creating cursor
conn = sqlite3.connect("signup.db")
c = conn.cursor()

# Data table
# c.execute(""" CREATE TABLE IF NOT EXISTS users(
#     Fullname TEXT,
#     Contact INTEGER,
#     Age INTEGER,
#     Email TEXT,
#     Password TEXT
# )""")
# conn.commit()

def submit():
    fullname = name.get()
    contact = cont.get()
    age_value = age.get()
    email = mail.get()
    password = pw.get()

    # Insert values into the database
    c.execute("INSERT INTO users (Fullname, Contact, Age, Email, Password) VALUES (?, ?, ?, ?, ?)",
              (fullname, contact, age_value, email, password))
    conn.commit()
    conn.close()

    # Clear the text boxes after pressing
    name.delete(0,END)
    cont.delete(0,END)
    age.delete(0,END)
    mail.delete(0,END)
    pw.delete(0,END)

    root.destroy()
    import loginpage as login

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Creating frame for all the labels and entryboxes
main_frame=Frame(root, width=1920, height=1080, bg="white",padx=150, pady=150)
main_frame.pack(fill=X, expand=True)

innerframe=Frame(main_frame, bg="white")
innerframe.pack()

# --------------------------------------------------------------------------------------------------------------------------------------------------

# User details
name_label = Label(innerframe,text="Full Name: ", font=("AppleGothic", 15), bg="white", fg="black")
name_label.grid(row=1,column=0, sticky="w", pady=10)

cont_label = Label(innerframe,text="Contact Number: ", font=("AppleGothic", 15), bg="white", fg="black")
cont_label.grid(row=2,column=0, sticky="w", pady=10)

age_label = Label(innerframe,text="Age: ", bg="white", font=("AppleGothic", 15), fg="black")
age_label.grid(row=3,column=0, sticky="w", pady=10)

mail_label = Label(innerframe,text="Email Address: ", font=("AppleGothic", 15), bg="white", fg="black")
mail_label.grid(row=4,column=0, sticky="w", pady=10)

# Password Entries
pw_label = Label(innerframe,text="New password: ", font=("AppleGothic", 15), bg="white", fg="black")
pw_label.grid(row=5,column=0, sticky="w", pady=25)

confirm_pw = Label(innerframe, text="Confirm password: ", font=("AppleGothic", 15), bg="white", fg="black")
confirm_pw.grid(row=6, column=0, sticky="w")

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Creating entry boxes
name=Entry(innerframe,width=30, font=("AppleGothic", 15), bg="white", fg="black")
name.grid(row=1,column=2, sticky="w", pady=10)

cont = Entry(innerframe,width=30, font=("AppleGothic", 15), bg="white", fg="black")
cont.grid(row=2,column=2, sticky="w", pady=10)

age = Entry(innerframe,width=30, font=("AppleGothic", 15), bg="white", fg="black")
age.grid(row=3,column=2, sticky="w", pady=10)

mail = Entry(innerframe,width=30, font=("AppleGothic", 15), bg="white", fg="black")
mail.grid(row=4,column=2, sticky="w", pady=10)

pw = Entry(innerframe,width=30, font=("AppleGothic", 15), bg="white", fg="black")
pw.grid(row=5,column=2, sticky="w", pady=25)

confirm_pw_entry = Entry(innerframe,width=30, font=("AppleGothic", 15), bg="white", fg="black")
confirm_pw_entry.grid(row=6,column=2, sticky="w")

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Submit button
register_btn = Button(innerframe,text="Register Now",font=('AppleGothic',15,'bold'), command=submit, bg="white", fg="black")
register_btn.grid(row=17,column=2,columnspan=2, ipady=10, ipadx=20, pady=70)

# For the bottom slogan
pic_img = Image.open("logo_slogan.png")
resized = pic_img.resize((700, 450),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(main_frame,image=new_logo, bd=0)
logo_label.pack(side='bottom', ipady=20)

root.mainloop()
