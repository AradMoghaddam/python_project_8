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

    for license in license_list:
        table.insert("", END, values=license)


def reset_form():
    id.set(len(license_list) + 1)
    name.set("")
    family.set("")
    serial.set(0)
    sader_date.set("")
    expired_date.set("")
    city.set("")

    load_data(license_list)


def save_btn_click():
    license = (id.get(), name.get(), family.get(), serial.get(),city.get(),sader_date.get(),expired_date.get())
    errors = license_validator(license)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "license saved")
        license_list.append(license)
        write_to_file("license.dat", license_list)
        reset_form()


def table_select(x, expired_date=None):
    selected_license = table.item(table.focus())["values"]
    if selected_license:
        id.set(selected_license[0])
        name.set(selected_license[1])
        family.set(selected_license[2])
        serial.set(selected_license[3])
        sader_date.set(selected_license[4])
        expired_date.set(selected_license[5])
        city.set(selected_license[6])


def edit_btn_click():
    pass


def remove_btn_click():
    pass


window = Tk()
window.title("license Info")
window.geometry("920x380")

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

Label(window, text="sader date").place(x=20, y=180)
sader_date = StringVar()
Entry(window, textvariable=sader_date).place(x=100, y=180)

Label(window, text="expired date").place(x=20, y=220)
expired_date = StringVar()
Entry(window, textvariable=expired_date).place(x=100, y=220)

Label(window, text="city").place(x=20, y=260)
city = StringVar()
Entry(window, textvariable=city).place(x=100, y=260)



table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6, 7],height=16, show="headings")
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
table.column(5, width=100)
table.column(6, width=100)
table.column(7, width=100)


table.bind("<<TreeviewSelect>>", table_select)

table.place(x=240, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=310)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=95, y=310)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=170, y=310)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=340, width=205)

reset_form()

window.mainloop()
