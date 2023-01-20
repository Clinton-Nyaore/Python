import tkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox

my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="lucid")
my_cursor = my_db.cursor()


def exitting():
    way_out = tkinter.messagebox.askyesno("Lucid Poultry Farm", "Do you want to exit the system?")
    if way_out > 0:
        root.destroy()
        return


def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Lucid Poultry Farm")
    root.geometry("1280x800+0+0")

    global name
    global phone
    global order

    name = StringVar()
    phone = StringVar()
    order = StringVar()

    frame1 = Frame(root, bg="yellow")
    frame1.place(x=0, y=0, width=540, relheight=1)

    frame2 = Frame(root, bg="grey")
    frame2.place(x=550, y=0, relwidth=1, relheight=1)

    Label(frame1, text="Lucid\nPoultry\nFarm", font=("times new roman", 70, "bold"), bg="yellow", fg="black").place(x=10,
                                                                                                            y=150)

    Label(frame2, text=":: Place Your Order Here ::", height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2",
          fg="white",
          bg="blue").place(x=90, y=90, width=350)

    Label(frame2, text="Your Name :", height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
          bg="gray").place(x=150, y=150, width=250)
    Entry(frame2, textvariable=name).place(x=150, y=210, width=250, height=30)
    Label(frame2, text="").pack()

    Label(frame2, text="Your Phone Number :", height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
          bg="gray").place(x=150, y=250, width=290)
    Entry(frame2, textvariable=phone).place(x=150, y=310, width=250, height=30)
    Label(frame2, text="").pack()

    Label(frame2, text="Your Order :", height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
          bg="gray").place(x=150, y=350, width=250)
    Entry(frame2, textvariable=order).place(x=150, y=410, width=250, height=35)
    Label(frame2, text="").pack()

    Button(frame2, text='Submit', height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
           bg="blue", command=submit_btn).place(x=150, y=470, width=250)
    Label(frame2, text="").pack()

    Button(frame2, text='Exit', height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
           bg="red", command=exitting).place(x=150, y=580, width=250)
    Label(frame2, text="").pack()


def submit_btn():
    the_name = name.get()
    the_phone = phone.get()
    the_order = order.get()

    my_str = [the_name, the_phone, the_order]

    if the_name == "" or the_phone == "" or the_order == "":
        messagebox.showinfo("Warning!", "Please input all values!")

    else:
        sql = """INSERT INTO customer_orders(name, phone, orders) 
                VALUES("%s", "%s", "%s")"""
        val = (my_str[0], my_str[1], my_str[2])
        my_cursor.execute(sql, val)

        my_db.commit()
        messagebox.showinfo("Success", f"""Thanks {my_str[0]} for Trusting Lucid Poultry Farm\n
        Your Order is {my_str[2]}""")



main_display()
mainloop()
