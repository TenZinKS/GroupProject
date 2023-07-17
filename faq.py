from tkinter import *
root = Tk()
root.title("Help and Support")
root.configure(bg='white')

# Setting window geometry to full screen
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

frame = LabelFrame(root, bg="white")
frame.pack(side="left",pady=5)

# TEXT IN  FRAME
text = Label(frame, text="Our FAQ's", font=("Helvetica", 30, "bold"), bg="white", fg="black")
text.grid(row=1, column=0, sticky="w")

text_1 = Label(frame, text="What is a period sathi, and why should I use one?", font=("Arial", 20, "bold"), bg="white", fg="black")
text_1.grid(row=2, column=0, sticky="w")

text_2 = Label(frame, text="A period sathi is a app or tool that helps you monitor and record your menstrual cycle.It allows you to track the start and end dates of your periods, along with other symptoms and patterns ", font=("Arial", 17), bg="white", fg="black")
text_2.grid(row=3, column=0, sticky="w")

text_3 = Label(frame, text="Using a period tracker can be beneficial because it helps you predict your next period, understand your menstrual patterns, and even identify potential health concerns. ", font=("Arial", 17), bg="white", fg="black")
text_3.grid(row=4, column=0, sticky="w")

text_4 = Label(frame, text="How do period trackers predict my menstrual cycle? ", font=("Arial", 20, "bold"), bg="white", fg="black")
text_4.grid(row=5, column=0, sticky="w")

text_5 = Label(frame, text="Period trackers use algorithms and data input by users to predict future periods based on the length of previous cycles.As you continue using tracker and recording your periods, it ", font=("Arial", 18), bg="white", fg="black")
text_5.grid(row=6, column=0, sticky="w")

text_6 = Label(frame, text="becomes more accurate in predicting when your next period will likely occur. ", font=("Arial", 18), bg="white", fg="black")
text_6.grid(row=7, column=0, sticky="w")

text_7 = Label(frame, text="Are period trackers accurate in predicting my periods? ", font=("Arial", 20, "bold"), bg="white", fg="black")
text_7.grid(row=8, column=0, sticky="w")

text_7 = Label(frame, text="N0, Period trackers can be reasonably accurate for many individuals, especially those with regular menstrual cycles.However, factors like stress, illness, travel, or hormonal changes ", font=("Arial", 18), bg="white", fg="black")
text_7.grid(row=9, column=0, sticky="w")

text_8 = Label(frame, text="can affect the predictability. It's essential to keep in mind that period trackers are not foolproof and may not work as well for those with irregular cycles. ", font=("Arial", 18), bg="white", fg="black")
text_8.grid(row=10, column=0, sticky="w")

text_9 = Label(frame, text="Can a period tracker help me get pregnant?", font=("Arial", 20, "bold"), bg="white", fg="black")
text_9.grid(row=11, column=0, sticky="w")

text_10 = Label(frame, text="YES,these fertility tracking features allow you to monitor ovulation and identify the most fertile days in your menstrual cycle, increasing your chances of getting pregnant. ", font=("Arial", 18), bg="white", fg="black")
text_10.grid(row=12, column=0, sticky="w")

text_11 = Label(frame, text="Can a period tracker help identify potential health issues? ", font=("Arial", 20, "bold"), bg="white", fg="black")
text_11.grid(row=13, column=0, sticky="w")

text_12 = Label(frame, text="Yes, keeping track of your menstrual cycle and related symptoms can be valuable in identifying potential health concerns.or instance, irregular periods or abnormal symptoms ", font=("Arial", 18), bg="white", fg="black")
text_12.grid(row=14, column=0, sticky="w")

text_13 = Label(frame, text="could be a sign of hormonal imbalances or other underlying health conditions. By showing your period tracking data to a healthcare professional, they may better understand your  ", font=("Arial", 18), bg="white", fg="black")
text_13.grid(row=15, column=0, sticky="w")

text_13 = Label(frame, text=" symptoms and provide appropriate advice or treatment.", font=("Arial", 18), bg="white", fg="black")
text_13.grid(row=16, column=0, sticky="w")

text_14 = Label(frame, text="Are period tracker apps safe to use? ", font=("Arial", 20, "bold"), bg="white", fg="black")
text_14.grid(row=17, column=0, sticky="w")

text_15 = Label(frame, text="Most period tracker apps are safe to use.However, it's essential to choose reputable and well-reviewed apps from reputable app stores.Read the app's privacy policy to understand  ", font=("Arial", 18), bg="white", fg="black")
text_15.grid(row=18, column=0, sticky="w")

text_16 = Label(frame, text="how they handle your data, as some apps may collect sensitive information. Always be cautious about sharing personal health data with third-party apps. ", font=("Arial", 18), bg="white", fg="black")
text_16.grid(row=19, column=0, sticky="w")

text_17 = Label(frame, text="What is PMS, and how can I manage its symptoms?", font=("Arial", 20, "bold"), bg="white", fg="black")
text_17.grid(row=20, column=0, sticky="w")

text_18 = Label(frame, text="Premenstrual Syndrome (PMS) refers to a combination of physical, emotional, and behavioral symptoms that some people experience before their periods. Common symptoms ", font=("Arial", 18), bg="white", fg="black")
text_18.grid(row=21, column=0, sticky="w")

text_19 = Label(frame, text="include mood swings, bloating, breast tenderness, fatigue, and irritability. To manage PMS, you can try regular exercise, a balanced diet, stress reduction techniques ", font=("Arial", 18), bg="white", fg="black")
text_19.grid(row=22, column=0, sticky="w")

text_20 = Label(frame, text="(like meditation or yoga), and over-the-counter pain relievers for discomfort.", font=("Arial", 18), bg="white", fg="black")
text_20.grid(row=23, column=0, sticky="w")

text_21 = Label(frame, text="What causes irregular periods, and when should I be concerned? ", font=("Arial", 20, "bold"), bg="white", fg="black")
text_21.grid(row=24, column=0, sticky="w")

text_22 = Label(frame, text="Irregular periods can have various causes, including hormonal imbalances, stress, changes in weight, medications, or medical conditions like polycystic ovary syndrome (PCOS).  ", font=("Arial", 18), bg="white", fg="black")
text_22.grid(row=25, column=0, sticky="w")

text_23 = Label(frame, text="Is it normal to have severe menstrual cramps? ", font=("Arial", 20, "bold"), bg="white", fg="black")
text_23.grid(row=26, column=0, sticky="w")

text_24 = Label(frame, text="Some degree of menstrual cramping is normal for many people during their periods. However, excessively painful cramps, can be a sign of an underlying condition or daily activities  ", font=("Arial", 18), bg="white", fg="black")
text_24.grid(row=27, column=0, sticky="w")

root.mainloop()