from tkinter import *

w=500
h=500
flh=150
tbw=300

root = Tk()
root.title("Nathair Level Generator")
editfull = Frame(root, width=w+tbw, height=h,)
editfull.pack(side=TOP)

finishedLvls =  Frame(root, width=w+tbw, height=flh, bg="red")
finishedLvls.pack(side=BOTTOM)

toolbar = Frame(editfull, width=tbw, height=h, bg="yellow")
toolbar.pack(side=RIGHT)

editwindow = Frame(editfull, width=w, height=h, bg="blue")
editwindow.pack(side=LEFT)

mainloop()