from tkinter import *
from random import randint
from tkinter import messagebox


root = Tk()
root.title("Password Generator")
root.geometry("500x300")


def new_rand():
    pw_entry.delete(0, END)

    pw_length = int(my_entry.get())

    my_password = ''

    for x in range(pw_length):
        my_password += chr(randint(33, 126))
    
    # output password
    pw_entry.insert(0,my_password)

# copy to clipboard
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    messagebox.showinfo("Copied", "Password copied to Clipboard")

lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

my_entry = Entry(lf, font=("helvertica", 24))
my_entry.pack(pady=20, padx=20)


pw_entry = Entry(root, text='',font="Helvertica, 24", bd=0, bg="lightgrey")
pw_entry.pack(pady=20)

# frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# buttons
my_button = Button(my_frame, text="Generate Password", command=new_rand)
my_button.grid(row=0, column=0, padx=5)

clip_button=Button(my_frame, text="copy to clipboard", command=clipper)
clip_button.grid(row=0,column=1, padx=5)




root.mainloop()