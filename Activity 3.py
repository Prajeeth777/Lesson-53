from tkinter import *

window=Tk()
window.title("Tkinter window")
window.geometry('600x400')

def topwin():
    top=Toplevel()
    top.geometry('200x200')
    top.title("Top level window")
    l1=Label(top,text="THis is top level window")
    l1.pack()
    top.mainloop()

l2=Label(window,text="This is root window")
button=Button(window,text="Click here to navigate to other window",command=topwin)
l2.pack()
button.pack()

window.mainloop()
