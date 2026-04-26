from tkinter import *

# button = ya click it , then it does stuff 

count = 0
def Click():
    global count 
    count += 1
    button.config(text=f"clicks: {count}")

window = Tk()

photo = PhotoImage(file=r"C:\Users\AL-AJIAL\Downloads\—Pngtree—3d facebook like icon on_20943730.png")
photo = photo.subsample(10,10)

button = Button(window,
                text="click me",
                command=Click,
                font=("commic sans",4),
                fg="red",
                bg="black",
                activeforeground="red",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='top')

button.pack()


window.mainloop()
