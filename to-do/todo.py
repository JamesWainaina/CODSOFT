#!/usr/bin/python3
from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title='To-Do-List'
        self.root.geometry("650x410+300+150")

        self.label = Label(self.root,text="To-Do-List", font="ariel, 25 bold", 
                           width=10,borderwidth=5, bg="blue", fg="white")
        self.label.pack(side="top" ,fill=BOTH)

        self.label2 = Label(self.root,text="Add Task", font="ariel, 10 bold", 
                           width=10,borderwidth=5, bg="blue", fg="white")
        self.label2.place(x=100, y= 64)

        self.label3 = Label(self.root,text="Tasks", font="ariel, 10 bold", 
                           width=10,borderwidth=5, bg="blue", fg="white")
        self.label3.place(x=420, y=64)

        self.main_text = Listbox(self.root,height=9,bd=5, width=23,font="ariel, 20 italic bold")

        self.main_text.place(x=280,y=100)

        self.text = Text(self.root,bd=5, height=2, width=30, font="ariel, 10 bold")

        self.text.place(x=20,y=120)

        def add():
            content = self.text.get(1.0,END)
            self.main_text.insert(END, content)
            with open("data.txt","a")as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete():
            selected_index = self.main_text.curselection()
            if selected_index:
                item = self.main_text.get(selected_index[0])
                self.main_text.delete(selected_index)
                with open("data.txt", "r+") as file:  # Open in read/write mode
                    lines = file.readlines()
                    file.seek(0)
                    for line in lines:
                        if item not in line:
                            file.write(line)
                    file.truncate()


        self.button = Button(self.root, text="ADD", font="sarif, 20 bold italic",
                              width= 10,bd=5, bg="blue", fg="white",command=add)
        
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="DELETE", font="sarif, 20 bold italic",
                              width= 10,bd=5, bg="blue", fg="white",command=delete)
        
        self.button2.place(x=30, y=280)

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == '__main__':
    main()