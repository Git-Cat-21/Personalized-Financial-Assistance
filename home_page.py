from tkinter import *

root=Tk()
root.geometry("600x600")
title=Label(root,text='Title')
title.pack(side=TOP)

signup = Button(root, text='Signup')
signup.place(x=375,y=40)
login = Button(root, text='Login')
login.place(x=420,y=40)
about_us = Button(root, text='About Us')
about_us.place(x=460,y=40)
contact_us = Button(root, text='Contact Us')
contact_us.place(x=520,y=40)
about_us_text=Label(root,text='About Us:')
about_us_text.place(x=0,y=100)
contact_us_text=Label(root,text='Contact Us:')
contact_us_text.place(x=0,y=200)

root.mainloop()