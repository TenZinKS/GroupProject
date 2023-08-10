from tkinter import *
import sqlite3
from PIL import Image, ImageTk

root=Tk()
root.title("Update Password")
root.configure(bg='white')
root.geometry("700x500")

# ------------------------------------------------------------------------------------------------------------

def update():
    try:
        # Connecting to the database and creating a cursor
        conn = sqlite3.connect("signup.db")
        c = conn.cursor()

        c.execute("""UPDATE users SET Password = :new_pw WHERE email = :myemail""",
                  {'new_pw': new_pw_entry.get(), 'myemail': mail_entry.get()}
        )

        # Committing and closing the database
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        if conn:
            conn.close()

    success = Label(root, text="Password updated successfully!\n You can close this window")
    success.configure(bg='white', fg='black', font=("AppleGothic",12))
    success.grid(row=4, column=1)

# ------------------------------------------------------------------------------------------------------------

# GUI

photoframe = Frame(root)
photoframe.grid(row=5, column=1)

# E-mail label and entry
myemail = Label(root, text="Enter your email: ")
myemail.configure(bg='white', fg='black', font=("AppleGothic",12))
myemail.grid(row=0, column=0, sticky='w')

mail_entry = Entry(root)
mail_entry.configure(bg='white', fg='black', font=("AppleGothic",12))
mail_entry.grid(row=0, column=1, pady=5)

# ------------------------------------------------------------------------------------------------------------

# Old password Label and Entry
old_pw = Label(root, text="Enter your old password: ")
old_pw.configure(bg='white', fg='black', font=("AppleGothic",12))
old_pw.grid(row=1, column=0, sticky='w')

old_pw_entry = Entry(root)
old_pw_entry.configure(bg='white', fg='black', font=("AppleGothic",12))
old_pw_entry.grid(row=1, column=1, pady=5)

# ------------------------------------------------------------------------------------------------------------

# New password Label and Entry
new_pw = Label(root, text="Enter your new password: ")
new_pw.configure(bg='white', fg='black', font=("AppleGothic",12))
new_pw.grid(row=2, column=0, sticky='w')

new_pw_entry = Entry(root)
new_pw_entry.configure(bg='white', fg='black', font=("AppleGothic",12))
new_pw_entry.grid(row=2, column=1, pady=5)

# ------------------------------------------------------------------------------------------------------------

# Update Button
update_btn = Button(root, command=update)
update_btn.configure(bg='white', fg='black', text='Update Password', font=("AppleGothic",14,"bold"))
update_btn.grid(row=3, column=1, pady=10)

pic_img = Image.open("logo_slogan.png")
resized = pic_img.resize((400, 250),Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
logo_label = Label(photoframe,image=new_logo, bd=0)
logo_label.pack(side='bottom')

root.mainloop()
