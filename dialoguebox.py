from tkinter import *
# from tkFileDialog import askopenfilename
from tkinter.filedialog import *
def callback():
    name = askopenfilename()
    print(name)

errmsg = "Error"
Button(text='File Open ',command =callback).pack(fill=X)
mainloop()