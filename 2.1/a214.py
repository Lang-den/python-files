from passlib.hash import pbkdf2_sha256
import tkinter, string

def submit_login():
    if user_input.get() not in users:
        result_label.config(text="There is no user with that name")
    elif pbkdf2_sha256.verify(pass_input.get(), users[user_input.get()]):
        result_label.config(text="You have successfully logged in")
    else:
        result_label.config(text='That is the wrong password')


def submit_sign_up():
    password = pass_input.get()

    if is_valid_password(password):
         result_label.config(text='Valid Sign up')
         if user_input.get() not in users:
            users[user_input.get()] = pbkdf2_sha256.hash(pass_input.get())
         else:
            result_label.config(text="Is already a user")
    else:
        result_label.config(text='NOT a valid Sign up')

def  is_valid_password(password):
    if len(password) < 8:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    return has_lower and has_digit and has_special and has_upper
        
users = {}

root = tkinter.Tk()
root.geometry("500x500")

user_label = tkinter.Label(root, text="Username:")
user_label.pack()
user_input = tkinter.Entry(root)
user_input.pack()

pass_label = tkinter.Label(root, text="Password:")
pass_label.pack()
pass_input = tkinter.Entry(root, #show="~"#
)
pass_input.pack()

login_button = tkinter.Button(root, text="Login", command=submit_login)
login_button.pack()

sign_up = tkinter.Button(root, text="Sign Up", command=submit_sign_up)
sign_up.pack()

result_label = tkinter.Label(root, text="Result goes here")
result_label.pack(pady=20)

root.mainloop()