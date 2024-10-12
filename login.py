from tkinter import *
from tkinter import font
from schemes import *

def print_data():
    print(user_id_entry.get())

def forgot_pwd():
    root=Tk()
    root.title('Forgot Password')
    user_id = Label(root, text='User ID:', font=('Arial', 14))
    user_id.grid(row=0, column=0, padx=20, pady=10, sticky=E)
    user_id_entry = Entry(root, font=('Arial', 12), width=25)
    user_id_entry.grid(row=0, column=1, padx=20, pady=10)

    pwd = Label(root, text='New Password:', font=('Arial', 14))
    pwd.grid(row=1, column=0, padx=20, pady=10, sticky=E)
    pwd_entry = Entry(root, font=('Arial', 12), width=25, show='*')
    pwd_entry.grid(row=1, column=1, padx=20, pady=10)

    conf_pwd = Label(root, text='Confirm Password:', font=('Arial', 14))
    conf_pwd.grid(row=2, column=0, padx=20, pady=10, sticky=E)
    conf_pwd_entry = Entry(root, font=('Arial', 12), width=25, show='*')
    conf_pwd_entry.grid(row=2, column=1, padx=20, pady=10)

    submit = Button(root, text='Submit', font=('Arial', 12), width=10, bg='lightblue')
    submit.grid(row=3, column=0, columnspan=2, pady=20)
    
    root.mainloop()

def login_page():
    global user_id_entry
    root = Tk()
    root.title("Login Page")
    root.geometry("1000x1000")

    title = Label(root, text='Login Page', font=('Arial', 20, 'bold'), bg='lightgrey', pady=10)
    title.pack(side=TOP, fill=X)

    form_frame = Frame(root, pady=10)
    form_frame.pack(pady=150)

    user_id = Label(form_frame, text='User ID:', font=('Arial', 14))
    user_id.grid(row=0, column=0, padx=20, pady=10, sticky=E)
    user_id_entry = Entry(form_frame, font=('Arial', 12), width=25)
    user_id_entry.grid(row=0, column=1, padx=20, pady=10)

    pwd = Label(form_frame, text='Password:', font=('Arial', 14))
    pwd.grid(row=1, column=0, padx=20, pady=10, sticky=E)
    pwd_entry = Entry(form_frame, font=('Arial', 12), width=25, show='*')
    pwd_entry.grid(row=1, column=1, padx=20, pady=10)

    submit = Button(form_frame, text='Login', font=('Arial', 12), width=10, bg='lightblue',command=schemes)
    submit.grid(row=2, column=0, columnspan=2, pady=20)

    forgot = Button(form_frame, text='Forgot Password?', font=font.Font(size=10, underline=True), borderwidth=0, fg='blue',command=forgot_pwd)
    forgot.grid(row=3, column=0, columnspan=2, pady=10)

    root.configure(bg='lightgrey')
    root.mainloop()

#login_page()