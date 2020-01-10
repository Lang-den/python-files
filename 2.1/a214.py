import tkinter

def printtext():
    print(name_input.get())

root = tkinter.Tk()
root.geometry("500x500")

user_label = tkinter.Label(root, text="Username:")
user_label.pack()

name_input = tkinter.Entry(root)
name_input.pack()

root.mainloop()