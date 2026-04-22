from tkinter import *

window = Tk()    # instantiate an instance of the window
window.geometry("300x300")
window.title("Hello")
window.config(background="black")


label = Label(window,
              text="Hello Programming",
              fg="blue",
              font=("Arial",40,"normal"),
              relief=RAISED,
              bd=10)


label.pack()


window.mainloop()

