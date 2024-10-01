from tkinter import *
from tkinter import font
root=Tk()
root.geometry("600x600")
title=Label(root,text='Login Page')
title.pack()
user_id=Label(root,text='User ID:')
user_id.place(x=230,y=100)
user_id_entry=Entry(root)
user_id_entry.place(x=300,y=100)

pwd=Label(root,text='Password:')
pwd.place(x=220,y=150)
pwd_entry=Entry(root)
pwd_entry.place(x=300,y=150)

submit=Button(root,text='Login')
submit.place(x=270,y=200)

forgot=Button(root,text='Forgot Password?',borderwidth=0,font=font.Font(size=10,underline=True))
forgot.place(x=240,y=230)

root.mainloop()