from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import random
from login import *  # Assuming login page is imported from a separate module

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import random
from login import *  # Assuming login page is imported from a separate module

def format_date(date):
    # Convert date from 'yyyy-mm-dd' to 'dd-mm-yyyy'
    month, day, year = date.split('/')
    return f"{day}/{month}/{year}"

def open_calendar():
    # Create a Toplevel window to act as a dropdown for the calendar
    top = Toplevel(root)
    top.title("Select Date")
    
    # Create a Calendar widget in the Toplevel window
    cal = Calendar(top, selectmode='day', year=2024, month=10, day=8)
    cal.pack(pady=20)
    
    # Button to insert the selected date into the text box
    def select_date():
        selected_date = cal.get_date()  # Gets the date in 'yyyy-mm-dd' format
        formatted_date = format_date(selected_date)  # Format it to 'dd-mm-yyyy'
        dob_entry.delete(0, END)  # Clear the entry before inserting the date
        dob_entry.insert(END, formatted_date)
        top.destroy()  # Close the calendar dropdown after date is selected
    
    # Button to confirm date selection
    select_btn = ttk.Button(top, text="Select", command=select_date)
    select_btn.pack(pady=10)

def open_calendar1():
    # Create a Toplevel window to act as a dropdown for the calendar
    top = Toplevel(root)
    top.title("Select Date")
    
    # Create a Calendar widget in the Toplevel window
    cal = Calendar(top, selectmode='day', year=2024, month=10, day=8)
    cal.pack(pady=20)
    
    # Button to insert the selected date into the text box
    def select_date():
        selected_date = cal.get_date()  # Gets the date in 'yyyy-mm-dd' format
        formatted_date = format_date(selected_date)  # Format it to 'dd-mm-yyyy'
        created_on_entry.delete(0, END)  # Clear the entry before inserting the date
        created_on_entry.insert(END, formatted_date)
        top.destroy()  # Close the calendar dropdown after date is selected
    
    # Button to confirm date selection
    select_btn = ttk.Button(top, text="Select", command=select_date)
    select_btn.pack(pady=10)

# (Rest of your code remains unchanged)


def create_user():
    rand_num = random.randint(100000, 999999)
    user_id.config(text=f"Your user ID is: {rand_num}")

def signup_page():
    global user_id
    global dob_entry
    global root
    global created_on_entry
    
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
    dob_entry = Entry(form_frame, font=('Arial', 12), width=25)  # Adjust width
    dob_entry.grid(row=3, column=1, padx=20, pady=10, sticky=W)    
    icon_btn = Button(form_frame, text="📅", font=("Arial", 12), command=open_calendar, borderwidth=0)
    icon_btn.grid(row=3, column=2, padx=5, pady=5, sticky=W)  # Positioned next to dob_entry


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
    icon_btn1 = Button(form_frame, text="📅", font=("Arial", 12), command=open_calendar1, borderwidth=0)
    icon_btn1.grid(row=4, column=5, padx=5, pady=5, sticky=W)  # Positioned next to dob_entry

    format = Label(form_frame, text='(in dd-mmm-yyyy)', font=('Arial', 10))
    format.grid(row=5, column=2, padx=20, pady=10, sticky=E)

    submit = Button(form_frame, text='Signup', font=('Arial', 12), command=create_user)
    submit.grid(row=6, column=0, columnspan=4, pady=20)

    user_id = Label(form_frame, text='', font=('Arial', 12), fg='blue')
    user_id.grid(row=7, column=0, columnspan=4, pady=10)

    return_back = Button(form_frame, text='Return to Login page', font=('Arial', 12, 'underline'), borderwidth=0, command=login_page)
    return_back.grid(row=8, column=0, columnspan=4, pady=20)

    root.configure(bg='lightgrey')
    root.mainloop()

signup_page()
