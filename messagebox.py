from tkinter import *
#from tkMessageBox import *

from tkinter.messagebox import *


def answer():
    showerror("Answer","sorry , no answer available")

def callback():
    if askyesno('verify','Really quit?'):
        showwarning('yes','Not yet implemented')
    else:
        showinfo('no','quit has been cancelled')

Button(text='Quit',command=callback).pack(fill=X)
Button(text='Answer',command=answer).pack(fill=X)
mainloop()