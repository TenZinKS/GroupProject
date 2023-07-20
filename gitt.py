from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Get in touch")
root.configure(bg='white')

# Set the window size (width x height)
window_width = 800
window_height = 600
root.geometry(f"800x600")

#Function to go back
def goback():
    root.destroy()
    import help_and_support as help

# TEXT
text = Label( text="OUR DEVELOPERS", font=("Comic sans", 32, "bold"), bg="white", fg="black")
text.grid(padx=260,row=1, column=0, sticky="w", pady=20)

text_2 = Label( text="Tenzin Kunsel Sherpa :", font=("Arial", 20,"bold" ), bg="white", fg="black")
text_2.grid(padx=260,row=2, column=0, sticky="w")

text_2 = Label( text="tenzinkuenzel2016@gmail.com, github.com/TenZinKS ", font=("Arial", 15), bg="white", fg="black")
text_2.grid(padx=260,row=3, column=0, sticky="w")

text_2 = Label( text="Abhinav Dhakal :", font=("Arial", 20,"bold" ), bg="white", fg="black")
text_2.grid(padx=260,row=4, column=0, sticky="w")

text_2 = Label( text="dhakalabhinav4@gmail.com, github.com/abhidhakal ", font=("Arial", 15), bg="white", fg="black")
text_2.grid(padx=260,row=5, column=0, sticky="w")

text_2 = Label( text="Aayam Bhattarai :", font=("Arial", 20,"bold" ), bg="white", fg="black")
text_2.grid(padx=260,row=6, column=0, sticky="w")

text_2 = Label( text="aayambhattarai3@gmail.com, github.com/aayam17 ", font=("Arial", 15), bg="white", fg="black")
text_2.grid(padx=260,row=7, column=0, sticky="w")

text_2 = Label( text="Soyesh Shrestha :", font=("Arial", 20,"bold" ), bg="white", fg="black")
text_2.grid(padx=260,row=8, column=0, sticky="w")

text_2 = Label( text="soyeshxrestha@gmail.com ", font=("Arial", 15), bg="white", fg="black")
text_2.grid(padx=260,row=9, column=0, sticky="w")

img = Image.open("logo_slogan.png")
resized = img.resize((450,200),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(root,image=new_logo, bd=0)
logo_label.grid(row=10, column=0, pady=10)


back_btn = Button(text="Back",command = goback)
back_btn.configure(width=5, height=2)
back_btn.grid(row=11,column=0)

root.mainloop()
