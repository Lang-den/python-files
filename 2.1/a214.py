import tkinter


def printtext():
    
    if len(pass_input.get()) >= 8 and len(pass_input.get()) <= 14:
        print('User:', user_input.get(),'\nPass:', pass_input.get())

root = tkinter.Tk()
root.geometry("500x500")

user_label = tkinter.Label(root, text="Username:")
user_label.pack()
user_input = tkinter.Entry(root)
user_input.pack()

pass_label = tkinter.Label(root, text="Password:")
pass_label.pack()
pass_input = tkinter.Entry(root, show="")
pass_input.pack()

submit_button = tkinter.Button(root, text="Submit", command=printtext)
submit_button.pack()

root.mainloop()