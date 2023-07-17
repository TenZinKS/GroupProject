from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Help and Support")
root.configure(bg='white')

# Setting window geometry to full screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))


def faq():
    import faq as openfaq


def gett():
    root.destroy()
    import gitt as letsgo



frame = LabelFrame(root, bg="white")
frame.pack(side="top", pady=5)

btn_frm = Frame(root, bg='white')
btn_frm.pack()

# TEXT IN  FRAME
text = Label(frame, text="Quick Guide:", font=("Helvetica", 32, "bold"), bg="white", fg="black")
text.grid(row=1, column=0, sticky="w")

text_1 = Label(frame, text="Getting Started : ", font=("Arial", 20, "bold", "underline"), bg="white", fg="black")
text_1.grid(row=2, column=0, sticky="w")

text_2 = Label(frame,
               text="Upon opening the app, you'll be prompted to set up your profile. Input your name, birthdate, and the average length of your menstrual cycle. Optionally, you can ",
               font=("Arial", 18,), bg="white", fg="black")
text_2.grid(row=3, column=0, sticky="w")

text_3 = Label(frame, text="include any relevant notes or symptoms you'd like to track throughout your cycle. ",
               font=("Arial", 18), bg="white", fg="black")
text_3.grid(row=4, column=0, sticky="w")

text_4 = Label(frame, text="Dashboard : ", font=("Arial", 20, "bold", "underline"), bg="white", fg="black")
text_4.grid(row=5, column=0, sticky="w")

text_5 = Label(frame,
               text="The app's home screen is your personalized dashboard, displaying crucial information about your current menstrual cycle. Here, you'll find the predicted start date .",
               font=("Arial", 18), bg="white", fg="black")
text_5.grid(row=6, column=0, sticky="w")

text_6 = Label(frame,
               text="of your next period and the expected fertile window. The dashboard also offers helpful insights into any recurring patterns or irregularities in in your cycle ",
               font=("Arial", 18), bg="white", fg="black")
text_6.grid(row=7, column=0, sticky="w")

text_7 = Label(frame, text="Calendar View : ", font=("Arial", 20, "bold", "underline"), bg="white", fg="black")
text_7.grid(row=8, column=0, sticky="w")

text_8 = Label(frame,
               text="Navigate to the calendar view to see a monthly overview of your menstrual cycle. Period days are marked with a distinctive color, making it easy to track your flow.",
               font=("Arial", 18), bg="white", fg="black")
text_8.grid(row=9, column=0, sticky="w")

text_9 = Label(frame, text="Tap on any day to add or edit symptoms, moods, or notes for that specific date. ",
               font=("Arial", 18), bg="white", fg="black")
text_9.grid(row=10, column=0, sticky="w")

text_10 = Label(frame, text="Symptom & Mood Tracking: ", font=("Arial", 20, "bold", "underline"), bg="white",
                fg="black")
text_10.grid(row=11, column=0, sticky="w")

text_11 = Label(frame,
                text="Keep track of your symptoms and moods throughout your cycle to identify patterns and understand your body better.Record symptoms like cramps, bloating, headaches, ",
                font=("Arial", 18), bg="white", fg="black")
text_11.grid(row=12, column=0, sticky="w")

text_12 = Label(frame,
                text="or any other physical experiences.Track moods like happiness, anxiety, irritability, and more, helping you manage emotional fluctuations effectively.",
                font=("Arial", 18), bg="white", fg="black")
text_12.grid(row=13, column=0, sticky="w")

text_13 = Label(frame, text="Alerts & Reminders: ", font=("Arial", 20, "bold", "underline"), bg="white", fg="black")
text_13.grid(row=14, column=0, sticky="w")

text_14 = Label(frame,
                text="Set notifications for the start of your period, fertile window, and any other events you'd like to remember.Never miss an important date with our customizable alerts and reminders.",
                font=("Arial", 18), bg="white", fg="black")
text_14.grid(row=15, column=0, sticky="w")

text_15 = Label(frame, text="Alerts & Reminders: ", font=("Arial", 20, "bold", "underline"), bg="white", fg="black")
text_15.grid(row=16, column=0, sticky="w")

text_16 = Label(frame,
                text="Discover trends in symptoms and moods that correlate with specific phases of your cycle.Track the duration and consistency of your cycles to detect irregularities.",
                font=("Arial", 18), bg="white", fg="black")
text_16.grid(row=17, column=0, sticky="w")

text_17 = Label(frame, text="Privacy & Security : ", font=("Arial", 20, "bold", "underline"), bg="white", fg="black")
text_17.grid(row=18, column=0, sticky="w")

text_18 = Label(frame,
                text="We understand the importance of privacy when it comes to personal health information.Rest assured that all your data is securely stored and never shared with third parties.",
                font=("Arial", 18), bg="white", fg="black")
text_18.grid(row=19, column=0, sticky="w")

text_19 = Label(frame, text="Educational Resources : ", font=("Arial", 20, "bold", "underline"), bg="white", fg="black")
text_19.grid(row=20, column=0, sticky="w")

text_20 = Label(frame,
                text="Explore comprehensive library of articles on women's health, menstrual hygiene, and overall well-being. ",
                font=("Arial", 18), bg="white", fg="black")
text_20.grid(row=21, column=0, sticky="w")

# Create a button and pack it into the main window
button1 = Button(btn_frm, text="Our FAQ's", width=25, height=5, command=faq)
button1.pack(side='left')

# Create a button and pack it into the main window
button2 = Button(btn_frm, text="Get in touch", width=25, height=5, command=gett)
button2.pack(side='right', anchor='w')

text_21 = Label(root,
                text="Remember, every individual's body is unique, and if you have specific concerns or questions about your health,\n it's essential to seek advice from a healthcare professional who can provide personalized guidance and support.",
                font=("Arial", 24), bg="white", fg="black")
text_21.pack(side='bottom', ipady=12)

root.mainloop()
