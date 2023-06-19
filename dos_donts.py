from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Do's and Dont's")
root.geometry("1440x900")

# Main Frame
frame = Frame(root, bg="white", height=900, width=1440)
frame.place(x=0,y=0)

# Function for when HomePage button is clicked
def returnhome():
    root.destroy()
    import Homepage as homeeeeee

# LOGO
logo_img = Image.open("logo_whitebg.png")
resized = logo_img.resize((250,170),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(frame,image=new_logo, bd=0)
logo_label.place(x=1200, y=0)

# TITLE
title = Label(frame, text="DO'S AND DONT'S", font=("Helvatica", 40,"bold"),bg="white", fg="black")
title.pack(side="top")

# FRAME FOR DO'S
do_frame = LabelFrame(frame, bg="white", height=600, width=700)
do_frame.pack(side="left", padx=10, pady=100)

# FRAME FOR DONT'S
dont_frame = LabelFrame(frame, bg="white", height=600, width=700)
dont_frame.pack(side="right", padx=10, pady=100)

# TEXT IN DO FRAME
do = Label(do_frame, text="Do:", font=("Comic Sans MS",32, "bold"),bg="white", fg="black")
do.grid(row=0, column=0, sticky="w")

point1 = Label(do_frame, text="Be Prepared", font=("Arial", 20, "underline"), bg="white", fg="black")
point1.grid(row=1, column=0, sticky="w", pady=5)

point2 = Label(do_frame, text="Light Exercises/Yoga", font=("Arial", 20, "underline"), bg="white", fg="black")
point2.grid(row=2, column=0, sticky="w", pady=5)

point3 = Label(do_frame, text="Stay hydrated", font=("Arial", 20, "underline"), bg="white", fg="black")
point3.grid(row=3, column=0, sticky="w", pady=5)

point4 = Label(do_frame, text="Keep your body tidy and neat", font=("Arial", 20, "underline"), bg="white", fg="black")
point4.grid(row=4, column=0, sticky="w", pady=5)

point5 = Label(do_frame, text="Change your pads frequently", font=("Arial", 20, "underline"), bg="white", fg="black")
point5.grid(row=5, column=0, sticky="w", pady=5)

point6 = Label(do_frame, text="Have healthy foods; greeen veggies, ginger, lentils", font=("Arial", 20, "underline"), bg="white", fg="black")
point6.grid(row=6, column=0, sticky="w", pady=5)

point7 = Label(do_frame, text="Have other comforting foods; dark chocolate, yogurt, kombucha, soups, noodles", font=("Arial", 20, "underline"), bg="white", fg="black")
point7.grid(row=7, column=0, sticky="w", pady=5)

point8 = Label(do_frame, text="Some cramp remedies: Hot compresses, stretching, medication, massages.", font=("Arial", 20, "underline"), bg="white", fg="black")
point8.grid(row=8, column=0, sticky="w", pady=5)

personal_note = Text(do_frame,height=15,width=50, border=True, bg="white", fg="black")
personal_note.insert(INSERT, "Personal Note: ")
personal_note.grid(row=9,column=0, pady=20)


# TEXT IN DONT FRAME

dont = Label(dont_frame, text="Dont:", font=("Comic Sans MS",32, "bold"),bg="white", fg="black")
dont.grid(row=0, column=0, sticky="w", pady=5)

point_1 = Label(dont_frame, text="If you discover something strange, try not to freak out or overthink it.", font=("Arial", 20, "underline"), bg="white", fg="black")
point_1.grid(row=1, column=0, sticky="w", pady=5)

point_2 = Label(dont_frame, text="Do not use old or expired pads or tampons.", font=("Arial", 20, "underline"), bg="white", fg="black")
point_2.grid(row=2, column=0, sticky="w", pady=5)

point_3 = Label(dont_frame, text="Avoid use of douching around the vaginal area,", font=("Arial", 20, "underline"), bg="white", fg="black")
point_3.grid(row=3, column=0, sticky="w", pady=5)

point_4 = Label(dont_frame, text="Do not eat too much spicy or sweet food, ignore your cravings.", font=("Arial", 20, "underline"), bg="white", fg="black")
point_4.grid(row=4, column=0, sticky="w", pady=5)

point_5 = Label(dont_frame, text="Do not avoid exercises or physical intimacy", font=("Arial", 20, "underline"), bg="white", fg="black")
point_5.grid(row=5, column=0, sticky="w", pady=5)

point_6 = Label(dont_frame, text="If you experience any symptoms like itching, burning, or unusual discharge, \nconsult a healthcare professional ASAP.", font=("Arial", 20, "underline"), bg="white", fg="black")
point_6.grid(row=6, column=0, pady=5)

point_7 = Label(dont_frame, text="Don't be ashamed of anything related to you or your body.", font=("Arial", 20, "underline"), bg="white", fg="black")
point_7.grid(row=7, column=0,sticky="w", pady=5)

personal__note = Text(dont_frame,height=15,width=50, border=True, bg="white", fg="black")
personal__note.insert(INSERT, "Personal Note: ")
personal__note.grid(row=8,column=0, pady=23)

# RETURN TO HOME BUTTON
homee = Button(root, text="HomePage", bg="white", fg="purple", command=returnhome)
homee.pack(side="bottom", pady=50)

root.mainloop()
