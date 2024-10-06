import mysql.connector
from tkinter import * 
from tkinter import ttk
from savings_dets import *

connection=mysql.connector.connect(host="localhost",user="root",password="password",database="pfa_orange")
cursor=connection.cursor()

cursor.execute("select * from schemes")

root_scheme=Tk()

root_scheme.title("Schemes")
root_scheme.geometry("800x800")

tree=ttk.Treeview(root_scheme)
tree["columns"]=("Scheme_ID","Scheme_Name","Rate of Interest","Duration_In_Years")
tree['show']='headings'
tree_style=ttk.Style(root_scheme)

tree_style.theme_use("clam")
tree_style.configure(".",font=("Helvetica",11))
tree_style.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,'bold'))

tree.column("Scheme_ID",width=150,minwidth=50,anchor=CENTER)
tree.column("Scheme_Name",width=200,minwidth=50,anchor=CENTER)
tree.column("Rate of Interest",width=150,minwidth=50,anchor=CENTER)
tree.column("Duration_In_Years",width=150,minwidth=50,anchor=CENTER)

tree.heading("Scheme_ID",text="Scheme_ID",anchor=CENTER)
tree.heading("Scheme_Name",text="Scheme_Name",anchor=CENTER)
tree.heading("Rate of Interest",text="Rate of Interest",anchor=CENTER)
tree.heading("Duration_In_Years",text="Duration_In_Years",anchor=CENTER)

tree.insert('',0,text="",values=("Scheme ID","Scheme Name","Rate of Interest","Duration in years"))
i=0
for row in cursor:
    tree.insert('',i,text="",values=(row[0],row[1],row[2],row[3]))
    i=i+1
tree.pack()

contact_us = Button(root_scheme, text='Proceed', font=('Arial', 12), bg='white', fg='black', padx=10,command=savings_dets)
contact_us.pack(side=RIGHT, padx=10)

root_scheme.mainloop()