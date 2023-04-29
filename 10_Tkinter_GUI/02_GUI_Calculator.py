import tkinter
from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry("400x450")
window.resizable(False, False)

num1 = IntVar()
num2 = IntVar()

mainTitle = Label(window, text="Calculator", font=("Arial", 25))
mainTitle.place(x=134, y=45)

# Text
type1 = Label(window, text="Type Value 1:", font=("Arial", 15))
type1.place(x=61, y=125)

type2 = Label(window, text="Type Value 2:", font=("Arial", 15))
type2.place(x=61, y=197)

resultLabel = Label(window, text="Result:", font=("Arial", 15))
resultLabel.place(x=118, y=336)


def Add():
    sum = num1.get() + num2.get()
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(sum))

def Diff():
    diff = num1.get() - num2.get()
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(diff))

def Mul():
    mul = num1.get() * num2.get()
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(mul))

def Div():
    div = num1.get() / num2.get()
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(div))

# Entries
entry1 = Entry(window, textvariable=num1)
entry1.place(x=200, y=130, height=25, width=143)

entry2 = Entry(window, textvariable=num2)
entry2.place(x=200, y=202, height=25, width=143)

resultEntry = Entry(window)
resultEntry.place(x=200, y=340, height=25, width=143)

# Buttons
buttonAdd = Button(window, text="+", fg="white", bg="green", font=("Arial", 14), command=Add)
buttonAdd.place(x=74, y=262, height=32, width=56)

buttonSub = Button(window, text="-", fg="white", bg="green", font=("Arial", 14), command=Diff)
buttonSub.place(x=142, y=262, height=32, width=56)

buttonMul = Button(window, text="x", fg="white", bg="green", font=("Arial", 14), command=Mul)
buttonMul.place(x=210, y=262, height=32, width=56)

buttonDiv = Button(window, text="/", fg="white", bg="green", font=("Arial", 14), command=Div)
buttonDiv.place(x=278, y=262, height=32, width=56)

window.mainloop()
