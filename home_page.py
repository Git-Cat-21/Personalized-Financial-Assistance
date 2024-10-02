from tkinter import *

root=Tk()
root.geometry("600x600")
root.title('Welcome page')

title=Label(root,text='Title',font=('Arial',16,'bold'))
title.pack(side=TOP)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)

signup = Button(root, text='Signup',font=('Arial',10))
signup.place(x=340,y=40)
login = Button(root, text='Login',font=('Arial',10))
login.place(x=390,y=40)
about_us = Button(root, text='About Us',font=('Arial',10))
about_us.place(x=430,y=40)
contact_us = Button(root, text='Contact Us',font=('Arial',10))
contact_us.place(x=495,y=40)
slideshow=Label(root,text='Slideshow:',font=('Arial',12))
slideshow.place(x=0,y=100)
about_us_text=Label(root,text='About Us:',font=('Arial',12))
about_us_text.place(x=0,y=200)
contact_us_text=Label(root,text='Contact Us:',font=('Arial',12))
contact_us_text.place(x=0,y=300)

root.mainloop()