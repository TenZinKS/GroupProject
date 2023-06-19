from tkinter import *
from PIL import Image, ImageTk

root = Tk() 
root.geometry("1920x1080")
root.title("SignUp")

title = Label(root, text="SIGN UP",fg="black", font=("Arial", 48, "bold"))
title.pack(side="top")

# Function after clicking signup
def signedup():
    root.destroy()
    import Homepage as home

# Function after clicking back to home
def logingo():
    root.destroy()
    import main as login

# Main Frame
frame=Frame(root, width=1920, height=1080, bg="white",padx=150, pady=150)
frame.pack(side="bottom")

# PERSONAL DETAILS

fullname=Label(frame, text="                 Full Name: ", font=("Arial", 15), bg="white", fg="black", pady=5).grid(row=1, column=1, sticky="w")
fullname_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=1, column=2, sticky="w")

contact=Label(frame, text="                 Contact: ", font=("Arial", 15), bg="white", fg="black", pady=5).grid(row=2, column=1, sticky="w")
contact_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=2, column=2, sticky="w")

age = Label(frame, text="                 Age: ", font=("Arial", 15), bg="white", fg="black", pady=5).grid(row=3, column=1, sticky="w")
age_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=3, column=2, sticky="w")

email = Label(frame, text="                 E-mail: ", font=("Arial", 15), bg="white", fg="black", pady=5).grid(row=4, column=1, sticky="w")
email_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=4, column=2, sticky="w")

# NEW PASSWORD
new_pw = Label(frame, text="                 New password: ", font=("Arial", 15), bg="white", fg="black").grid(row=5, column=1, sticky="w")
new_pw_entry = Entry(frame, width=25, show="*", bg="white", fg="black").grid(row=5, column=2, pady=20, sticky="w")

confirm_pw = Label(frame, text="                 Confirm password: ", font=("Arial", 15), bg="white", fg="black").grid(row=6, column=1, sticky="w")
confirm_pw_entry = Entry(frame, width=25, show="*", bg="white", fg="black").grid(row=6, column=2, sticky="w")

# QUESTIONS
last_period = Label(frame, text="                 Your Last Period: ", font=("Arial", 15), bg="white", fg="black", pady=50).grid(row=7, column=1, sticky="w")
last_period_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=7, column=2, sticky="w")

pills = Label(frame, text="                 Do you take pills?", font=("Arial", 15), bg="white", fg="black").grid(row=8, column=1, sticky="w")
pills = Checkbutton(frame, bg="white", fg="black").grid(row=8, column=2, sticky="w")

last_pill = Label(frame, text="                 Your last pill intake: ", font=("Arial", 15), bg="white", fg="black", pady=50).grid(row=9, column=1, sticky="w")
last_pill_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=9, column=2, sticky="w")

# SIGNUP BUTTON
signup=Button(frame,text="Register Now",fg="#a94da0",relief=RAISED, bg="white", pady=10, width=11, command=signedup)
signup.grid(row=10,column=2, sticky="w")

# RETURN TO LOGIN BUTTON
home = Button(frame, text="Return To Login", fg="#a94da0",relief=RAISED, bg="white", pady=10, width=11, command=logingo)
home.grid(row=11, column=2, sticky="w", pady=20)

root.mainloop()
