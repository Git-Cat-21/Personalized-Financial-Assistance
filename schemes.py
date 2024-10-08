import mysql.connector
from tkinter import * 
from tkinter import ttk
from savings_dets import *

def calc():
    id = scheme_id_entry.get()
    amt = int(amount_entry.get())
    
    cursor.execute(f"select Interest_Rate, Duration_In_Years from schemes WHERE Scheme_ID={id};")
    values = cursor.fetchall()
    int_rate = values[0][0]
    duration = values[0][1]
    int_amt = (int_rate * amt) / 100

    global tot_int
    tot_int = int_amt * duration

    global tot_amt
    tot_amt = duration * (int_amt + amt)

    interest_amt_entry.delete(0, END)
    interest_amt_entry.insert(0, tot_int)
    
    tot_amount_entry.delete(0, END)
    tot_amount_entry.insert(0, tot_amt)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="pfa_orange"
)
cursor = connection.cursor()

cursor.execute("select * from schemes")


def schemes():
    global scheme_id_entry
    global amount_entry
    global interest_amt_entry
    global tot_amount_entry

    root_scheme = Tk()
    root_scheme.title("Schemes")
    root_scheme.geometry("800x800")
    root_scheme.configure(bg="#f0f0f0")

    tree = ttk.Treeview(root_scheme)
    tree["columns"] = ("Scheme_ID", "Scheme_Name", "Rate of Interest", "Duration_In_Years")
    tree['show'] = 'headings'

    tree_style = ttk.Style(root_scheme)
    tree_style.theme_use("clam")
    tree_style.configure(".", font=("Helvetica", 11))
    tree_style.configure("Treeview.Heading", foreground='blue', font=("Helvetica", 12, 'bold'))

    tree.column("Scheme_ID", width=150, minwidth=50, anchor=CENTER)
    tree.column("Scheme_Name", width=200, minwidth=50, anchor=CENTER)
    tree.column("Rate of Interest", width=150, minwidth=50, anchor=CENTER)
    tree.column("Duration_In_Years", width=150, minwidth=50, anchor=CENTER)

    tree.heading("Scheme_ID", text="Scheme ID", anchor=CENTER)
    tree.heading("Scheme_Name", text="Scheme Name", anchor=CENTER)
    tree.heading("Rate of Interest", text="Rate of Interest", anchor=CENTER)
    tree.heading("Duration_In_Years", text="Duration in Years", anchor=CENTER)

    i = 0
    for row in cursor:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3]))
        i += 1
    tree.pack(pady=20)

    form_frame = Frame(root_scheme, pady=20, bg="#f0f0f0")
    form_frame.pack(pady=50)

    scheme_id = Label(form_frame, text='Scheme ID :', font=('Arial', 12), bg="#f0f0f0")
    scheme_id.grid(row=0, column=0, padx=20, pady=10, sticky=E)
    scheme_id_entry = Entry(form_frame, font=('Arial', 12), width=25)
    scheme_id_entry.grid(row=0, column=1, padx=20, pady=10)

    amount = Label(form_frame, text='Amount :', font=('Arial', 12), bg="#f0f0f0")
    amount.grid(row=1, column=0, padx=20, pady=10, sticky=E)
    amount_entry = Entry(form_frame, font=('Arial', 12), width=25)
    amount_entry.grid(row=1, column=1, padx=20, pady=10)

    interest_amt = Label(form_frame, text='Interest Amount :', font=('Arial', 12), bg="#f0f0f0")
    interest_amt.grid(row=2, column=0, padx=20, pady=10, sticky=E)
    interest_amt_entry = Entry(form_frame, font=('Arial', 12), width=25)
    interest_amt_entry.grid(row=2, column=1, padx=20, pady=10)

    tot_amount = Label(form_frame, text='Total Amount :', font=('Arial', 12), bg="#f0f0f0")
    tot_amount.grid(row=3, column=0, padx=20, pady=10, sticky=E)
    tot_amount_entry = Entry(form_frame, font=('Arial', 12), width=25)
    tot_amount_entry.grid(row=3, column=1, padx=20, pady=10)

    def on_enter(e):
        calc_button['background'] = '#00cc66'
        calc_button['foreground'] = 'white'

    def on_leave(e):
        calc_button['background'] = '#f0f0f0'
        calc_button['foreground'] = 'black'

    calc_button = Button(form_frame, text="Calculate", font=('Arial', 12, 'bold'), bg="#f0f0f0", fg="black", command=calc)
    calc_button.grid(row=4, columnspan=2, pady=20)

    trans_history = Button(form_frame, text='My Transactions', font=('Arial', 12), bg='white', fg='black', padx=10,command=transactions)
    trans_history.grid(row=5, columnspan=2, pady=20)

    calc_button.bind("<Enter>", on_enter)
    calc_button.bind("<Leave>", on_leave)

    proceed_button = Button(form_frame, text="Proceed", font=('Arial', 12, 'bold'), bg="#f0f0f0", fg="black", command=savings_dets)
    proceed_button.grid(row=6, columnspan=2, pady=20)

    exit_button = Button(form_frame, text="Exit", font=('Arial', 12, 'bold'), bg="#f0f0f0", fg="black", command=root_scheme.destroy)
    exit_button.grid(row=7, columnspan=2, pady=20)

    root_scheme.mainloop()