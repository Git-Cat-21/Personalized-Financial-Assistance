from tkinter import *

root=Tk()
frame=Frame(root)
frame.pack()
signup = Button(frame, text='Signup')
signup.pack()
login = Button(frame, text='Login')
login.pack()
about_us = Button(frame, text='About Us')
about_us.pack()
contact_us = Button(frame, text='Contact Us')#below scroll
contact_us.pack()
root.mainloop()