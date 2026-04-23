from tkinter import *

# button = ya click it , then it does stuff 

count = 0
def Click():
    global count 
    count += 1
    button.config(text=f"clicks: {count}")

window = Tk()

button = Button(window,
                text="click me",
                command=Click)

button.pack()


window.mainloop()
