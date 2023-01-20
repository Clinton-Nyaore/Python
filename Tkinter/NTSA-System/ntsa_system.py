from tkinter import *
from tkinter import messagebox, PhotoImage, Image
import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="ntsa")
my_cursor = my_db.cursor()


def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("NTSA")
    root.geometry("500x500")

    global img, name, password
    name = str()
    password = str()

    img = PhotoImage(file="logo.png")

    Button(root, image=img).pack(side=TOP)
    Label(root, text="").pack()

    Label(root, text="Login to View Your Details", fg="black", font=('arial', 12, 'bold')).pack()
    Label(root, text="").pack()

    Label(root, text="Name :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=name).pack()
    Label(root, text="").pack()


    Label(root, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=password, show="*").pack()
    Label(root, text="").pack()

    Button(root, text="Login", bg="green", fg='white', relief="groove",
           font=('arial', 12, 'bold'), command=logged).pack()
    Label(root, text="").pack()

    Button(root, text='Exit', height="1", width="20",font=('arial', 12, 'bold'), cursor="hand2", fg="red",
           bg="green", command=exitting).pack()
    Label(root, text="").pack()


def logged_destroy():
    logged_message.destroy()
    root.destroy()


def failed_destroy():
    failed_message.destroy()


def logged():
    my_cursor.execute("SELECT * FROM user_ntsa")
    myresult = my_cursor.fetchall()
    global x
    for x in myresult:
        x += x

    my_cursor.execute("SELECT * FROM details_ntsa")
    my_result = my_cursor.fetchall()
    global y
    for y in my_result:
        y += y

    global logged_message
    logged_message = Toplevel(root)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="""Login Successfully!... Welcome {} 
     to NTSA Portal,\n your licence number is {}\n{}""".format(x[1], y[1], y[2]), fg="blue",
          font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Logout", bg="green", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=logged_destroy).pack()


def exitting():
    way_out = messagebox.askyesno("NTSA", "Do you want to exit the system?\nWelcome Again!")
    if way_out > 0:
        root.destroy()
        return


main_display()
mainloop()
