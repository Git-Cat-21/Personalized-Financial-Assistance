from tkinter import * 

def savings_dets():
    root_savings_dets=Tk()
    root_savings_dets.title("Savings Details")
    root_savings_dets.geometry("950x950")

    title = Label(root_savings_dets, text='Savings Details', font=('Arial', 20, 'bold'), bg='lightgrey', pady=10)
    title.pack(side=TOP, fill=X)

    form_frame = Frame(root_savings_dets, pady=20)
    form_frame.pack(pady=50)

    user_id = Label(form_frame, text='User ID :', font=('Arial', 12))
    user_id.grid(row=0, column=0, padx=20, pady=10, sticky=E)
    user_id_entry = Entry(form_frame, font=('Arial', 12), width=25)
    user_id_entry.grid(row=0, column=1, padx=20, pady=10)

    acc_no = Label(form_frame, text='Account Number :', font=('Arial', 12))
    acc_no.grid(row=1, column=0, padx=20, pady=10, sticky=E)
    acc_no_entry = Entry(form_frame, font=('Arial', 12), width=25)
    acc_no_entry.grid(row=1, column=1, padx=20, pady=10)

    mobile = Label(form_frame, text='Mobile Number :', font=('Arial', 12))
    mobile.grid(row=2, column=0, padx=20, pady=10, sticky=E)
    mobile_entry = Entry(form_frame, font=('Arial', 12), width=25)
    mobile_entry.grid(row=2, column=1, padx=20, pady=10)

    amount = Label(form_frame, text='Amount :', font=('Arial', 12))
    amount.grid(row=3, column=0, padx=20, pady=10, sticky=E)
    amount_entry = Entry(form_frame, font=('Arial', 12), width=25)
    amount_entry.grid(row=3, column=1, padx=20, pady=10)

    pan = Label(form_frame, text='PAN Number :', font=('Arial', 12))
    pan.grid(row=0, column=2, padx=20, pady=10, sticky=E)
    pan_entry = Entry(form_frame, font=('Arial', 12), width=25, show='*')
    pan_entry.grid(row=0, column=3, padx=20, pady=10)

    mat_amt = Label(form_frame, text='Maturity Amount :', font=('Arial', 12))
    mat_amt.grid(row=1, column=2, padx=20, pady=10, sticky=E)
    mat_amt_entry = Entry(form_frame, font=('Arial', 12), width=25, show='*')
    mat_amt_entry.grid(row=1, column=3, padx=20, pady=10)

    inv_date = Label(form_frame, text='Invested On :', font=('Arial', 12))
    inv_date.grid(row=2, column=2, padx=20, pady=10, sticky=E)
    inv_date_entry = Entry(form_frame, font=('Arial', 12), width=25)
    inv_date_entry.grid(row=2, column=3, padx=20, pady=10)

    mat_date = Label(form_frame, text='Maturity Date :', font=('Arial', 12))
    mat_date.grid(row=3, column=2, padx=20, pady=10, sticky=E)
    mat_date_entry = Entry(form_frame, font=('Arial', 12), width=25)
    mat_date_entry.grid(row=3, column=3, padx=20, pady=10)

    root_savings_dets.configure(bg='lightgrey')

    submit = Button(form_frame, text='Submit', font=('Arial', 12),command=root_savings_dets.destroy)
    submit.grid(row=6, column=0, columnspan=4, pady=20)

    root_savings_dets.mainloop()


savings_dets()