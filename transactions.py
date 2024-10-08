from tkinter import *

def transactions():
    root_trans=Tk()
    root_trans.title("Transactions History")
    root_trans.geometry("500x500")

    exit = Button(root_trans, text='Exit', font=('Arial', 12), bg='white', fg='black', padx=10,command=root_trans.destroy)
    exit.pack(side=LEFT, padx=10)

    root_trans.mainloop()
