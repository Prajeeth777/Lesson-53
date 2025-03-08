from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Tkinter Image")
window.geometry('600x400')

def msg():
  messagebox.showwarning("Alert","Virus Detected!")

button=Button(window,text="Click Here!",command=msg)
button.pack()

window.mainloop()
