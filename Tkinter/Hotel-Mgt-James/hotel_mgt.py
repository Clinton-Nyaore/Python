import tkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox

my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
my_cursor = my_db.cursor()


def order():
    global root2
    root2 = Toplevel(root)
    root2.title("Your Order")
    root2.geometry("450x300")
    root2.config(bg="white")

    global name
    global myorder
    Label(root2, text='Please Enter your Order', bd=5, font=('arial', 12, 'bold'), relief="groove",
          fg="white",
          bg="maroon", width=300).pack()
    name = str()
    myorder =  str()
    Label(root2, text="").pack()

    Label(root2, text="Enter Your Name :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=name).pack()
    Label(root2, text="").pack()

    Label(root2, text="Enter Your Order:", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=myorder).pack()
    Label(root2, text="").pack()

    Button(root2, text="Submit", bg="maroon", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=submitted_info).pack()
    Label(root2, text="")
    sql = "INSERT INTO yourorder(name, myorder) VALUES(%s, %s)"
    val = (name, myorder)
    my_cursor.execute(sql, val)
    my_db.commit()

def submit_destroy():
    submit_message.destroy()
    root2.destroy()


def submitted_info():
    global submit_message
    submit_message = Toplevel(root2)
    submit_message.title("Welcome")
    submit_message.geometry("500x100")

    my_list = []
    my_cursor.execute("SELECT * FROM yourorder")

    my_result = my_cursor.fetchone()
    for x in my_result:
        my_list.append(x)
        x += x

    Label(submit_message, text="Welcome {}\n to The  Avena Hotel.\nYour Order is {}".format(my_list[1], my_list[2]), fg="black",
          font="bold").pack()
    Label(submit_message, text="").pack()
    Button(submit_message, text="Logout", bg="brown", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=submit_destroy).pack()


def exitting():
    way_out = tkinter.messagebox.askyesno("The  Avena Hotel",
                                          "Do you want to exit the system?\nHope you enjoyed our service")
    if way_out > 0:
        root.destroy()
        return


def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("The  Avena Hotel")
    root.geometry("500x500")

    Label(root, text="The  Avena Hotel", bd=20, font=("arial", 20, "bold"), bg="brown", fg="blue", width=300).pack()
    Label(root, text="").pack()

    Button(root, text='Your Order Tab', height="1", width="20", bd=8, font=('arial', 12, 'bold'), cursor="hand2", fg="white",
           bg="blue", command=order).pack()
    Label(root, text="").pack()

    Button(root, text='Exit', height="1", width="20", bd=8, font=('arial', 12, 'bold'), cursor="hand2", fg="red",
           bg="blue", command=exitting).pack()
    Label(root, text="").pack()


main_display()
mainloop()
