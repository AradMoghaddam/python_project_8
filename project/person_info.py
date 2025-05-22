from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from jax.example_libraries.stax import serial

from file_manager import *
from validator import *

license_list = read_from_file("license.dat")


def load_data(license_list):
    license_list = read_from_file("license.dat")
    for row in table.get_children():
        table.delete(row)

    for person in license_list:
        table.insert("", END, values=person)


def reset_form():
    id.set(len(license_list) + 1)
    name.set("")
    family.set("")
    serial.set("")
    sader_date.set("")
    expired_date.set("")
    city.set("")

    load_data(license_list)


def save_btn_click():
    person = (id.get(), name.get(), family.get(), serial.get(),city.get(),sader_date.get(),expired_date.get())
    errors = license_validator(license)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "license saved")
        license_list.append(license)
        write_to_file("license.dat", license_list)
        reset_form()


def table_select(x, expired_date=None):
    selected_person = table.item(table.focus())["values"]
    if selected_person:
        id.set(selected_person[0])
        name.set(selected_person[1])
        family.set(selected_person[2])
        serial.set(selected_person[3])
        sader_date.set(selected_person[4])
        expired_date.set(selected_person[5])
        city.set(selected_person[6])


def edit_btn_click():
    pass


def remove_btn_click():
    pass


window = Tk()
window.title("license Info")
window.geometry("1200x370")

# Id
Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=100, y=20)

# Name
Label(window, text="name").place(x=20, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=60)

# Family
Label(window, text="family").place(x=20, y=100)
family = StringVar()
Entry(window, textvariable=family).place(x=100, y=100)

# Account
Label(window, text="serial").place(x=20, y=140)
serial = IntVar()
Entry(window, textvariable=serial).place(x=100, y=140)

Label(window, text="sader_date").place(x=20, y=180)
sader_date = IntVar()
Entry(window, textvariable=sader_date).place(x=100, y=180)

Label(window, text="expired_date").place(x=20, y=220)
expired_date = IntVar()
Entry(window, textvariable=expired_date).place(x=100, y=220)

Label(window, text="city").place(x=20, y=260)
city = StringVar()
Entry(window, textvariable=city).place(x=100, y=260)



table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6, 7], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="serial")
table.heading(5, text="Sader Date")
table.heading(6, text="expired Date")
table.heading(7, text="city")







table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)


table.bind("<<TreeviewSelect>>", table_select)

table.place(x=230, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=300)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=90, y=300)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=160, y=300)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=330, width=190)

reset_form()

window.mainloop()
