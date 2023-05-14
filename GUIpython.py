""" Done by Dhananjay S Panth [dhananjaypanth95@gmail.com]"""

from tkinter import *
import calendar


def displaycalendar():
    newroot = Tk()
    newroot.title("calendar screen")
    newroot.config(bg="dark blue")
    newroot.geometry("700x700")
    actualyear = int(yearentry.get())
    calendarcontent = calendar.calendar(actualyear)
    lblnew = Label(newroot, text=calendarcontent, font="consolas 10 bold")
    lblnew.grid(row=0, column=0, padx=30, pady=30)
    newroot.mainloop()


root = Tk()
root.config(bg="dark blue")
root.title("calendar app")
root.geometry("400x400")

header = Label(
    root, text="CALENDAR", bg="yellow", fg="brown", font=("times", 32, "bold")
)

header.grid(row=0, column=0, padx=25, pady=25)

lbl = Label(root, text="Enter the year: ")
lbl.grid(row=1, column=0, padx=25)

yearentry = Entry(root, width=5)
yearentry.grid(row=2, column=0, padx=25, pady=10)

showcalendar = Button(
    root, text="show calendar", fg="dark green", command=displaycalendar
)

showcalendar.grid(row=3, column=0, padx=2)

exitButton = Button(root, text="Exit", fg="purple", command=root.destroy)
exitButton.grid(row=4, column=0, padx=25)

root.mainloop()
