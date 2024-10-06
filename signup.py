from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import random
from login import *

def create_user():
    rand_num = random.randint(100000, 999999)
    user_id.config(text=f"Your user id is: {rand_num}")

def signup_page():
    global user_id
    root = Tk()
    root.title('Signup Page')
    root.geometry("1000x1000")

    title = Label(root, text='Signup Page', font=('Arial', 20, 'bold'), bg='lightgrey', pady=10)
    title.pack(side=TOP, fill=X)

    form_frame = Frame(root, pady=20)
    form_frame.pack(pady=50)

    name = Label(form_frame, text='Name:', font=('Arial', 12))
    name.grid(row=0, column=0, padx=20, pady=10, sticky=E)
    name_entry = Entry(form_frame, font=('Arial', 12), width=25)
    name_entry.grid(row=0, column=1, padx=20, pady=10)

    mob = Label(form_frame, text='Mobile number:', font=('Arial', 12))
    mob.grid(row=1, column=0, padx=20, pady=10, sticky=E)
    mob_entry = Entry(form_frame, font=('Arial', 12), width=25)
    mob_entry.grid(row=1, column=1, padx=20, pady=10)

    email = Label(form_frame, text='Email:', font=('Arial', 12))
    email.grid(row=2, column=0, padx=20, pady=10, sticky=E)
    email_entry = Entry(form_frame, font=('Arial', 12), width=25)
    email_entry.grid(row=2, column=1, padx=20, pady=10)

    dob = Label(form_frame, text='Date of birth:', font=('Arial', 12))
    dob.grid(row=3, column=0, padx=20, pady=10, sticky=E)
    dob_entry = Entry(form_frame, font=('Arial', 12), width=25)
    dob_entry.grid(row=3, column=1, padx=20, pady=10)

    pwd = Label(form_frame, text='Password:', font=('Arial', 12))
    pwd.grid(row=4, column=0, padx=20, pady=10, sticky=E)
    pwd_entry = Entry(form_frame, font=('Arial', 12), width=25, show='*')
    pwd_entry.grid(row=4, column=1, padx=20, pady=10)

    conf_pwd = Label(form_frame, text='Confirm Password:', font=('Arial', 12))
    conf_pwd.grid(row=5, column=0, padx=20, pady=10, sticky=E)
    conf_pwd_entry = Entry(form_frame, font=('Arial', 12), width=25, show='*')
    conf_pwd_entry.grid(row=5, column=1, padx=20, pady=10)

    acc_no = Label(form_frame, text='Account number:', font=('Arial', 12))
    acc_no.grid(row=0, column=2, padx=20, pady=10, sticky=E)
    acc_no_entry = Entry(form_frame, font=('Arial', 12), width=25)
    acc_no_entry.grid(row=0, column=3, padx=20, pady=10)

    ifsc = Label(form_frame, text='IFSC Code:', font=('Arial', 12))
    ifsc.grid(row=1, column=2, padx=20, pady=10, sticky=E)
    ifsc_entry = Entry(form_frame, font=('Arial', 12), width=25)
    ifsc_entry.grid(row=1, column=3, padx=20, pady=10)

    status = Label(form_frame, text='Account status:', font=('Arial', 12))
    status.grid(row=2, column=2, padx=20, pady=10, sticky=E)
    statuss = ['Active', 'Inactive']
    status_entry = ttk.Combobox(form_frame, values=statuss, width=22, font=('Arial', 12))
    status_entry.grid(row=2, column=3, padx=20, pady=10)

    type = Label(form_frame, text='Account type:', font=('Arial', 12))
    type.grid(row=3, column=2, padx=20, pady=10, sticky=E)
    types = ["Savings", "Current"]
    type_entry = ttk.Combobox(form_frame, values=types, width=22, font=('Arial', 12))
    type_entry.grid(row=3, column=3, padx=20, pady=10)

    created_on = Label(form_frame, text='Account created on:', font=('Arial', 12))
    created_on.grid(row=4, column=2, padx=20, pady=10, sticky=E)
    created_on_entry = Entry(form_frame, font=('Arial', 12), width=25)
    created_on_entry.grid(row=4, column=3, padx=20, pady=10)

    format = Label(form_frame, text='(in dd-mmm-yyyy)', font=('Arial', 10))
    format.grid(row=5, column=2, padx=20, pady=10, sticky=E)

    submit = Button(form_frame, text='Signup', font=('Arial', 12), command=create_user)
    submit.grid(row=6, column=0, columnspan=4, pady=20)

    return_back = Button(form_frame, text='Login Now', font=('Arial', 12),command=login_page)
    return_back.grid(row=8, column=0, columnspan=4,pady=20)

    root.configure(bg='lightgrey')
    root.mainloop()

# signup_page()