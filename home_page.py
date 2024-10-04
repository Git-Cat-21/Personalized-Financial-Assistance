from tkinter import *
from login import *
from signup import *
def update_text_slideshow():
    global text_index
    text_index += 1
    
    if text_index >= len(text_list):  # If the index exceeds the list, restart
        text_index = 0
    
    new_text = text_list[text_index]
    slideshow_content.config(text=new_text)  # Update the text in the label
    
    root.after(2000, update_text_slideshow)


text_list = [
    "Welcome to the Tkinter Slideshow!",
    "This is a simple text-based slideshow.",
    "You can display any text here.",
    "Each message will change every 2 seconds.",
    "Enjoy creating your Tkinter applications!"
]
text_index=0
root = Tk()
root.title('Welcome Page')
root.geometry("1000x1000")
root.configure(bg='lightgrey')

title = Label(root, text='Welcome to Our Platform', font=('Arial', 24, 'bold','underline'), bg='lightgrey', fg='black', pady=10)
title.pack(side=TOP, fill=X)

nav_frame = Frame(root, bg='lightgrey')
nav_frame.pack(side=TOP, anchor='ne', padx=20, pady=20)
contact_us = Button(nav_frame, text='Contact Us', font=('Arial', 12), bg='white', fg='black', padx=10)
contact_us.pack(side=RIGHT, padx=10)
about_us = Button(nav_frame, text='About Us', font=('Arial', 12), bg='white', fg='black', padx=10)
about_us.pack(side=RIGHT, padx=10)
login = Button(nav_frame, text='Login', font=('Arial', 12), bg='white', fg='black', padx=10,command=login_page)
login.pack(side=RIGHT, padx=10)
signup = Button(nav_frame, text='Signup', font=('Arial', 12), bg='white', fg='black', padx=10,command=signup_page)
signup.pack(side=RIGHT, padx=10)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

content_frame = Frame(root, bg='lightgrey')
content_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
slideshow_content = Label(content_frame, text=text_list[text_index], font=('Arial', 16), bg='lightgrey', relief=SOLID, wraplength=500, padx=20, pady=20)
slideshow_content.pack(fill=X, pady=5)
about_us_text = Label(content_frame, text='About Us:', font=('Arial', 16, 'bold'), bg='lightgrey', anchor='w')
about_us_text.pack(fill=X, pady=10)
about_us_details = Label(content_frame, text='We are a leading company in the tech industry, providing innovative solutions.', font=('Arial', 12), bg='lightgrey',relief=SOLID,wraplength=550, padx=10, pady=5)
about_us_details.pack(fill=X, pady=5)
contact_us_text = Label(content_frame, text='Contact Us:', font=('Arial', 16, 'bold'), bg='lightgrey', anchor='w')
contact_us_text.pack(fill=X, pady=10)
contact_us_details = Label(content_frame, text='Email: contact@ourcompany.com\nPhone: +91 9238465728', font=('Arial', 12), bg='lightgrey', relief=SOLID, wraplength=550, padx=10, pady=5)
contact_us_details.pack(fill=X, pady=5)
content_frame.after(2000, update_text_slideshow) 
root.mainloop()
