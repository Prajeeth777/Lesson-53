from tkinter import *
from PIL import Image,ImageTk

window=Tk()
window.title("Tkinter Image")
window.geometry('600x400')

upload=Image.open('LeBron.jpeg')
image=ImageTk.PhotoImage(upload)

label=Label(window,image=image)
label.pack()

window.mainloop()
