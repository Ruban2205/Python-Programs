from tkinter import *

window = Tk()
window.title("URK20CS1054 Area Calculator")
window.geometry("500x500")
window.resizable(False, False)

# Labels
side1 = Label(window, text="Side A: ", font=("Arial", 16))
side1.place(x=127, y=137)

side2 = Label(window, text="Side B: ", font=("Arial", 16))
side2.place(x=127, y=200)

side3 = Label(window, text="Side C: ", font=("Arial", 16))
side3.place(x=127, y=263)

area = Label(window, text="The Area is: ", font=("Arial", 12))
area.place(x=125, y=415)

perimeter = Label(window, text="The Perimeter is: ", font=("Arial", 11))
perimeter.place(x=125, y=449)

# Radiobutton
i = IntVar()
circleRadio = Radiobutton(window, text="Circle", value=1, variable=i)
circleRadio.place(x=98, y=43)

triangleRadio = Radiobutton(window, text="Triangle", value=2, variable=i)
triangleRadio.place(x=204, y=43)

rectangleRadio = Radiobutton(window, text="Rectangle", value=3, variable=i)
rectangleRadio.place(x=324, y=43)


# Functon
def triangleArea():
    sideA = int(entry1.get())
    sideB = int(entry2.get())

    radioBtn2 = triangleRadio
    areaEntry = entry4
    perimeterEntry = entry5
    if i.get() == 2:
        area = sideA * sideB / 2
        sideC = int(entry3.get())
        perimeter = sideA + sideB + sideC
        areaEntry.delete(0, END)
        areaEntry.insert(0, area)
        perimeterEntry.delete(0, END)
        perimeterEntry.insert(0, perimeter)
    else:
        areaEntry.delete(0, END)
        areaEntry.insert(0, "Please select the option correctly!")
        perimeterEntry.delete(0, END)
        perimeterEntry.insert(0, "Please select the option correctly!")


# def trianglePerimeter():
#     SideA = int(entry1.get())
#     SideB = int(entry2.get())
#     SideC = int(entry3.get())
#     radioBtn2 = triangleRadio
#     perimeterEntry = entry5
#
#     if i.get() == 2:
#         perimeter = SideA + SideB + SideC
#         perimeterEntry.delete(0, END)
#         perimeterEntry.insert(0, perimeter)
#
#     else:
#         perimeterEntry.delete(0, END)
#         perimeterEntry.insert(0, "Please select the option correctly ")


# Buttons
calculateBtn = Button(window, text="Calculate", command=triangleArea)
calculateBtn.place(x=246, y=326, width=96, height=33)

# Entries
entry1 = Entry(window)
entry1.place(x=216, y=137, width=157, height=23)

entry2 = Entry(window)
entry2.place(x=216, y=200, width=157, height=23)

entry3 = Entry(window)
entry3.place(x=215, y=263, width=157, height=23)

entry4 = Entry(window)
entry4.place(x=240, y=415, width=146, height=23)

entry5 = Entry(window)
entry5.place(x=240, y=447, width=146, height=23)

window.mainloop()