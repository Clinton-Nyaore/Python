from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="mybank")
my_cursor = my_db.cursor()

def action():
    my_list = []
    my_cursor.execute("SELECT * FROM customers")

    my_result = my_cursor.fetchone()
    for x in my_result:
        my_list.append(x)

    def clear():
        ac.delete(0, END)
        name.delete(0, END)
        amount.delete(0, END)
        mobile.delete(0, END)
        others.delete(0, END)
    ac = my_list[1]
    if ac == "":
        messagebox.showerror("Error", "Enter Account Number", parent=des)
    else:
        for i in my_list:
            if ac == my_list[1]:
                messagebox.showinfo("Success", "Successfully Found Account Number", parent=des)
                data_name = my_list[2]
                data_amount = my_list[3]
                data_mobile = my_list[4]
            

                name = Label(des, text="Name :", font='sans-serif 14 bold', bg="#CD5C5C")
                name.place(x=200, y=160, anchor='e')

                amount = Label(des, text="Amount :", font='sans-serif 14 bold', bg="#CD5C5C")
                amount.place(x=200, y=220, anchor='e')

                mobile = Label(des, text="Mobile No :", font='sans-serif 14 bold', bg="#CD5C5C")
                mobile.place(x=200, y=280, anchor='e')

                funds = Label(des, text="Source Of Funds :", font='sans-serif 14 bold', bg="#CD5C5C")
                funds.place(x=200, y=330, anchor='e')

                name = Entry(des, bd=5, width=40, font='sans-serif 14 bold', textvariable=name)
                name.place(x=220, y=144)
                name.insert(0, data_name)

                amount = Entry(des, bd=5, width=40, font='sans-serif 14 bold', textvariable=amount)
                amount.place(x=220, y=205)
                amount.insert(0, data_amount)

                mobile = Entry(des, bd=5, width=40, font='sans-serif 14 bold', textvariable=mobile)
                mobile.place(x=220, y=262)
                mobile.insert(0, data_mobile)

                Radio_button_sal = Radiobutton(des, text='Salary', value="salary", font='sans-serif 10 bold',
                                               variable=var)
                Radio_button_sal.place(x=220, y=320)
                var.set('salary')

                Radio_button_vah = Radiobutton(des, text='Vehicle Sale', value="vehicle", font='sans-serif 10 bold',
                                               variable=var)
                Radio_button_vah.place(x=220, y=350)

                Radio_button_pro = Radiobutton(des, text='Property Sale', value="property", font='sans-serif 10 bold',
                                               variable=var)
                Radio_button_pro.place(x=220, y=380)

                

                clear = Button(des, text="Clear", font='Verdana 13 bold', command=clear)
                clear.place(x=760, y=85)
                break
            else:
                messagebox.showerror("Error", "Enter a Correct Account Number", parent=des)
                break


def scan():
    messagebox.showinfo("Scan", "This Services Coming Soon", parent=des)


def disable_event():
    pass


def cancel():
    way_out = messagebox.askyesno("Usaidizi Bank System", "Do you want to exit the system?")
    if way_out > 0:
        des.destroy()
        return

des = Tk()
des.title("Usaidizi Bank System")
des.geometry("1280x800+0+0")

des.config(bg='yellow')

f = Frame(des, height=580, width=1180, bg='green')
f.place(x=10, y=10)

ac = StringVar()
name = StringVar()
amount = IntVar(des, value='0')
var = StringVar()
mobile = StringVar()


Label(des, text="Usaidizi Bank", bd=20, font=("arial", 20, "bold"), bg="yellow", fg="blue", width=300).pack()
Label(des, text="").pack()

ac_no = Label(des, text="Account No :", font='sans-serif 14 bold', bg="#CD5C5C")
ac_no.place(x=200, y=100, anchor='e')

ac = Entry(des, bd=5, width=40, font='sans-serif 14 bold', textvariable=ac)
ac.focus()
ac.place(x=220, y=85)

a = Frame(des, height=1, width=240, bg="white")
a.place(x=880, y=120)

b = Frame(des, height=330, width=1, bg="white")
b.place(x=880, y=120)

c = Frame(des, height=1, width=240, bg="white")
c.place(x=880, y=450)

d = Frame(des, height=330, width=1, bg="white")
d.place(x=1120, y=120)

enter = Button(des, text="Enter", font='Verdana 13 bold', command=action)
enter.place(x=680, y=85)

scan = Button(des, text="Scan", font='Verdana 13 bold', width=12, height=6, command=scan)
scan.place(x=830, y=130)

cancel = Button(des, text="Cancel", font='Verdana 13 bold', width=12, height=6, command=cancel)
cancel.place(x=830, y=295)

des.mainloop()
