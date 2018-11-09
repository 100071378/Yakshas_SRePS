from tkinter import *

OPTIONS = [
"Product ID",
"Category",
"Name",
"Brand"
]

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0])

w = OptionMenu(master, variable, *OPTIONS)
w.pack()


def ok():
    print("value is:" + variable.get())


button = Button(master, text="OK", command=ok)
button.pack()

mainloop()