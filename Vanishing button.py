from tkinter import *
def vanish(event):
    button.pack_forget()
window = Tk()
button = Button(window, text = "Click me")
button.pack(padx = 10, pady = 10)
button.bind("<ButtonReleased-1>", vanish)
window.mainloop()
