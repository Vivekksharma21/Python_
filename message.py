from tkinter import *
main = Tk()
ourMessage='I am vivek kumar'
messageVar=Message(main,text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop()