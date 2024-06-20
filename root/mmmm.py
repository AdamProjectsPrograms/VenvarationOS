import os
from tkinter import *
def run():
    os.system('cls')
    root = Tk()
    root.state('zoomed')
    LabelFrame(root, width=8289919, height=50, bg='black').place(x=0, y=0)
    Label(root, text='VenvarationOS', fg='white', bg='black').place(x=30, y=15)
    Label(root, text=open('root/account/username.usr').readlines()[0], fg='white', bg='black').place(x=130, y=15)
    root.mainloop()