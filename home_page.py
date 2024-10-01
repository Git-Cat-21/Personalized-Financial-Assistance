from tkinter import *

root=Tk()
root.title('Title')
root.geometry("500x500")
frame=Frame(root,width=500,height=500)
frame.pack()
title

signup = Button(frame, text='Signup')
signup.pack()
login = Button(frame, text='Login')
login.pack()
about_us = Button(frame, text='About Us')
about_us.pack()
contact_us = Button(frame, text='Contact Us')
contact_us.pack()
# about_us_text=Text(frame,text='About Us')
# about_us_text.pack()
root.mainloop()