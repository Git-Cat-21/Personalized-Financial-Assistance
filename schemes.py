import mysql.connector
from tkinter import * 
from tkinter import ttk

connection=mysql.connector.connect(host="localhost",user="root",password="mysql@123",database="pfa_orange")
cursor=connection.cursor()




cursor.execute("select * from schemes")


root_scheme=Tk()

root_scheme.title("Schemes")
root_scheme.geometry("800x800")

tree=ttk.Treeview(root_scheme)
tree["columns"]=("Scheme_Name","Rate of Interest","Duration")
tree['show']='headings'
tree_style=ttk.Style(root_scheme)

tree_style.theme_use("clam")
tree_style.configure(".",font=("Helvetica",11))
tree_style.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,'bold'))

tree.column("Scheme_Name",width=200,minwidth=50,anchor=CENTER)
tree.column("Rate of Interest",width=150,minwidth=50,anchor=CENTER)
tree.column("Duration",width=150,minwidth=50,anchor=CENTER)

tree.heading("Scheme_Name",text="Scheme_Name",anchor=CENTER)
tree.heading("Rate of Interest",text="Rate of Interest",anchor=CENTER)
tree.heading("Duration",text="Duration",anchor=CENTER)

tree.insert('',0,text="",values=("Scheme Name","Rate of Interest","Duration"))
i=0
for row in cursor:
    tree.insert('',i,text="",values=(row[0],row[1],row[2]))
    i=i+1
tree.pack()
root_scheme.mainloop()