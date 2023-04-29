import turtle
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

window = Tk()
window.title("URK20CS2001 - Registration Form")
window.geometry("700x380")
window.resizable(False, False)

# Labels
mainTitle = Label(window, text="Registration Form", fg="black", font=("Arial", 35))
mainTitle.place(x=29, y=25)

nameLabel = Label(window, text="Full Name", fg="black", font=("Arial", 16))
nameLabel.place(x=29, y=89)

emailLabel = Label(window, text="Email", fg="black", font=("Arial", 16))
emailLabel.place(x=29, y=134)

genderLabel = Label(window, text="Gender", fg="black", font=("Arial", 16))
genderLabel.place(x=29, y=179)

countryLabel = Label(window, text="Country", fg="black", font=("Arial", 16))
countryLabel.place(x=29, y=224)

programmingLabel = Label(window, text="Programming", fg="black", font=("Arial", 16))
programmingLabel.place(x=29, y=269)

# Entries
nameEntry = Entry(window)
nameEntry.place(x=191, y=90, height=24, width=468)

emailEntry = Entry(window)
emailEntry.place(x=191, y=135, height=24, width=468)

# Combo Box for Country
countryEntry = Combobox(window, values=["select your country",
                                        "Canada",
                                        "Ireland",
                                        "India",
                                        "Italy",
                                        "Malaysia",
                                        "Sri Lanka",
                                        "Singapore",
                                        "United States"])
print(dict(countryEntry))
countryEntry.current(0)
countryEntry.place(x=191, y=225, height=24, width=167)

# Radio Buttons

genderButton2 = Radiobutton(window, text="Female", value=1)
genderButton2.place(x=283, y=183)

genderButton1 = Radiobutton(window, text="Male", value=2)
genderButton1.place(x=191, y=183)

programmingButton1 = Checkbutton(window, text="Java")
programmingButton1.place(x=191, y=272)

programmingButton2 = Checkbutton(window, text="Python")
programmingButton2.place(x=283, y=272)


def submit():
    name = nameEntry.get()
    email = emailEntry.get()
    country = countryEntry.get()

    if len(name) == 0 or len(email) == 0 or len(country) == 0:
        messagebox.showerror(title="Error", message="All the fields are mandatory!!")

    else:
        messagebox.showinfo(title="Successful", message="Registration Success!!")


# Submit Button
submitButton = Button(window, text="Submit", bg="red", fg="white", font=("Arial", 16), command=submit)
submitButton.place(x=29, y=314, width=108, height=38)

window.mainloop()
