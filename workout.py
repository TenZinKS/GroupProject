from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image

root = Tk()
root.title("Workout")
root.configure(bg='white')

width= root.winfo_screenwidth()
height= root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

# ---------------------------------------------------------------------------------------------------------------------------------------

def gohome():
    root.destroy()
    import home_frontend

# ---------------------------------------------------------------------------------------------------------------------------------------

# FRAMES
# Scrollbar Frame
scrollframe = Frame(root, bg='black')
scrollframe.pack(side=RIGHT, fill=Y)

# Workouts Frame
woframe = LabelFrame(root, bg='white', fg='black')
woframe.pack(anchor='nw',ipady=10, ipadx=27)

# Label
label5=Label(root, text=" Yoga Exercises which helps during Menstrual Cramps:")
label5.configure(bg='white', fg='black', font=('Arial', 20, 'bold'))
label5.pack(anchor="w",pady=25)

# Yoga Frame
yogaframe = LabelFrame(root,bg='white', fg='black', bd=0)
yogaframe.pack(anchor='sw', ipadx=10, ipady=15)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Labels for the workouts
label=Label(woframe, text="Best exercises to do during periods: ")
label.configure(bg='white', fg='black', font=('Helvetica', 20, 'bold'))
label.grid(row=0, column=0, pady=10, sticky="w")

walk=Label(woframe, text="1: WALKING \nA simple, light walk is the best exercise you can do during your periods. \nThis low-intensity aerobic exercise helps your lungs work properly later in your cycle.  ")
walk.configure(bg='white', fg='black', font=('Arial', 12))
walk.grid(pady=5,row=1, column=0, sticky='n', padx=20)

running=Label(woframe, text="2: RUNNING \n Yes, running! In the later days of your periods or when you have mild symptoms,\n you can go running. Go for a slow run and take some breaks in between if you feel uncomfortable.\n Running can reduce your pain and irritability instantly. \nRemember to keep yourself well hydrated. ")
running.configure(bg='white', fg='black', font=('Arial', 12))
running.grid(pady=5,row=1, column=1, padx=15)

yog=Label(woframe, text="3: YOGA \nYoga can relax your cranky and irritable mood just by stretching and breathing \nexercises. Many yoga poses help to increase your blood circulation and provide ease to your noxious\n complaints. It is scientifically proven and tested that yoga \ahelps to relax your body and relieve your\n period symptoms such as cramps and bloating.  ")
yog.configure(bg='white', fg='black', font=('Arial', 12))
yog.grid(pady=5,row=1, column=2, padx=15)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Pictures below the workouts

walkimg = Image.open("walk.png")
resized = walkimg.resize((200,300),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(woframe,image=new_logo)
logo_label.grid(row=2, column=0) 

runimg = Image.open("run.png")
resized1 = runimg.resize((200,300),Image.LANCZOS)
new_logo1 = ImageTk.PhotoImage(resized1)
logo_label1 = Label(woframe,image=new_logo1)
logo_label1.grid(row=2, column=1)

yogimg = Image.open("yoga.png")
resized2 = yogimg.resize((250,300),Image.LANCZOS)
new_logo2 = ImageTk.PhotoImage(resized2)
logo_walk = Label(woframe,image=new_logo2)
logo_walk.grid(row=2, column=2)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Labels for yoga pose/ stretches

# Headers for each poses
cobra_head = Label(yogaframe, text=" COBRA POSE (Picture 1):")
cobra_head.configure(bg='white', fg='black', font=('Arial', 13, 'bold'))
cobra_head.grid(row=1,column=0, pady=10)

cow_head = Label(yogaframe, text=" COW POSE (Picture 2):")
cow_head.configure(bg='white', fg='black', font=('Arial', 13, 'bold'))
cow_head.grid(row=1,column=1)

cat_head = Label(yogaframe, text=" CAT POSE (Picture 3):")
cat_head.configure(bg='white', fg='black', font=('Arial', 13, 'bold'))
cat_head.grid(row=1,column=2)

fish_head = Label(yogaframe, text="FISH POSE (Picture 4):")
fish_head.configure(bg='white', fg='black', font=('Arial', 13, 'bold'))
fish_head.grid(row=1,column=3)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Pose details
label7=Label(yogaframe, text="Lie on your stomach with your legs straight and feet together,\nand place your hands under your shoulders.\n Using your hands to push you, lift your head and shoulders.\n Breathe deeply.Hold this pose for 30 to 60 seconds,\nas long as you feel comfortable.\n Then return to your original lying Breathing should be deep.\nTry to completely fill the belly when you breathe ")
label7.configure(bg='white', fg='black', font=('Arial', 13))
label7.grid(row = 2,column= 0,pady=10, padx=10, sticky="n")

label8=Label(yogaframe, text="Get on your hands and knees.\n Make sure your hands are directly under your shoulders,\nand your knees are directly under your hips. Take a deep breath in,\n and lower your belly toward the ground, while you gently stretch your head \nand bottom to the This is a cow pose.  ")
label8.configure(bg='white', fg='black', font=('Arial', 13))
label8.grid(row = 2,column= 1,pady=10, padx=10, sticky="n")

label9=Label(yogaframe, text="Breathe normally for 2 to 3 breaths.\n When you are ready to change your position,inhale deeply, \nthen as you breathe out, curl your back toward the sky,\n with your head and bottom gently stretching towards the ground.\n This is a cat pose.")
label9.configure(bg='white', fg='black', font=('Arial', 13))
label9.grid(row = 2,column= 2,pady=10, padx=10, sticky="n")

label10=Label(yogaframe, text="Place a pillow on the floor. Place your back and head on the pillow\n and place your legs straight in front of you on the floor.\n Place your arms comfortably at your sides, with your palms facing up.\n Stay in this pose, breathing gently, as long as you feel comfortable.\n If having the legs straight causes low back discomfort,\n please bend the knees with feet flat on the floor.")
label10.configure(bg='white', fg='black', font=('Arial', 13))
label10.grid(row = 2,column= 3,pady=10, padx=10, sticky="n")

# ---------------------------------------------------------------------------------------------------------------------------------------

# Yoga pose pictures
cobraimg = Image.open("cobrap.png")
resized3 = cobraimg.resize((300,200),Image.LANCZOS)
new_logo3 = ImageTk.PhotoImage(resized3)
logo_label3 = Label(yogaframe,image=new_logo3)
logo_label3.grid(row=3, column=0)

cowimg = Image.open("cowp.png")
resized4 = cowimg.resize((300,200),Image.LANCZOS)
new_logo4 = ImageTk.PhotoImage(resized4)
logo_label4 = Label(yogaframe,image=new_logo4)
logo_label4.grid(row=3, column=1)

catimg = Image.open("catp.png")
resized5 = catimg.resize((300,200),Image.LANCZOS)
new_logo5 = ImageTk.PhotoImage(resized5)
logo_label5 = Label(yogaframe,image=new_logo5)
logo_label5.grid(row=3, column=2)

fishimg = Image.open("fishp.png")
resized6 = fishimg.resize((300,200),Image.LANCZOS)
new_logo6 = ImageTk.PhotoImage(resized6)
logo_label6 = Label(yogaframe,image=new_logo6)
logo_label6.grid(row=3, column=3)

# ---------------------------------------------------------------------------------------------------------------------------------------

home_btn = Button(yogaframe, command=gohome)
home_btn.configure(height=2, width=10,bg='white', fg='black', text="Go Back", font=("Arial", 12, "bold"))
home_btn.grid(row=4, column=3, pady=15, padx=15)

root.mainloop()
