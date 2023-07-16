from tkinter import *

root = Tk()
root.geometry("1920x1080")

bg = PhotoImage(file="suptheme.png")
pic_label = Label(root, image=bg)
pic_label.place(x=0, y=0, relwidth=1, relheight=1)

frame=Frame(root, width=500, height=500, bg="white")
frame.place(x=440, y=80 )

Label(frame, text="SIGN UP", bg="white", fg="black", font=("Comic Sans MS", 36, "bold"), pady=40).grid(row=0, column=2)

a = Label(frame, bg="white", fg="black").grid(row=0, column=0)

fullname=Label(frame, text="                 Full Name: ", font=("Arial", 15), bg="white", fg="black", pady=5).grid(row=1, column=1)
fullname_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=1, column=2)

contact=Label(frame, text="                 Contact: ", font=("Arial", 15), bg="white", fg="black", pady=5).grid(row=2, column=1)
contact_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=2, column=2)

age = Label(frame, text="                 Age: ", font=("Arial", 15), bg="white", fg="black", pady=5).grid(row=3, column=1)
age_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=3, column=2)

email = Label(frame, text="                 E-mail: ", font=("Arial", 15), bg="white", fg="black", pady=5).grid(row=4, column=1)
email_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=4, column=2)

new_pw = Label(frame, text="                 New password: ", font=("Arial", 15), bg="white", fg="black").grid(row=5, column=1)
new_pw_entry = Entry(frame, width=25, show="*", bg="white", fg="black").grid(row=5, column=2, pady=20)

confirm_pw = Label(frame, text="                 Confirm password: ", font=("Arial", 15), bg="white", fg="black").grid(row=6, column=1)
confirm_pw_entry = Entry(frame, width=25, show="*", bg="white", fg="black").grid(row=6, column=2)

#Questions
last_period = Label(frame, text="                 Your Last Period: ", font=("Arial", 15), bg="white", fg="black", pady=50).grid(row=7, column=1)
last_period_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=7, column=2)

pills = Label(frame, text="                 Do you take pills?", font=("Arial", 15), bg="white", fg="black").grid(row=8, column=1)
pills = Checkbutton(frame, bg="white", fg="black").grid(row=8, column=2)

last_pill = Label(frame, text="                 Your last pill intake: ", font=("Arial", 15), bg="white", fg="black", pady=50).grid(row=9, column=1)
last_pill_entry = Entry(frame, width=25, bg="white", fg="black").grid(row=9, column=2)

signup=Button(frame,text="Register Now",fg="#a94da0",relief=RAISED, bg="white", pady=10)
signup.grid(row=10,column=2)

# lol=Label(frame, text="                      ", pady=30, bg="white").grid(row=10, column=1)


root.mainloop()
