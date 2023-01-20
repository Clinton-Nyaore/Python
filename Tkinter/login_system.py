import tkinter
from tkinter import *
#import mysql.connector
from tkinter import messagebox

#mydb = mysql.connector.connect(host="localhost", user="root2", passwd="Clintonnyaore", database="logindb")
#cursordb = mydb.cursor()


def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="white")

    global username_verification
    global password_verification
    Label(root2, text='Please Enter your Account Details', bd=5, font=('arial', 12, 'bold'), relief="groove",
          fg="white",
          bg="green", width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="green", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=login_verification).pack()
    Label(root2, text="")


def logged_destroy():
    logged_message.destroy()
    root2.destroy()


def failed_destroy():
    failed_message.destroy()


def logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="blue",
          font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Logout", bg="green", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=logged_destroy).pack()


def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message, text="Ok", bg="green", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=failed_destroy).pack()


def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from usertable where username = %s and password = %s"
    cursordb.execute(sql, [user_verification, pass_verification])
    results = cursordb.fetchall()
    if results:
        for _ in results:
            logged()
            break
    else:
        failed()


def exitting():
    way_out = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system?")
    if way_out > 0:
        root.destroy()
        return


def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("1280x800+0+0")

    frame1 = Frame(root, bg="yellow")
    frame1.place(x=0, y=0, width=450, relheight=1)

    frame2 = Frame(root, bg="gray95")
    frame2.place(x=450, y=0, relwidth=1, relheight=1)

    frame3 = Frame(frame2, bg="white")
    frame3.place(x=140, y=150, width=500, height=450)

    Label(frame1, text="Login", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(x=100,
                                                                                                   y=200)
    Label(frame1, text="\nSystem", font=("times new roman", 40, "bold"), bg="yellow",
          fg="red").place(x=162, y=300)
    Label(frame1, text=":: Welcome Clinton ::", font=("times new roman", 25, "bold"), bg="yellow",
          fg="blue").place(x=80, y=300)

    Button(frame3, text='Log In', height="3", width="20", bd=8, font=('arial', 25, 'bold'), cursor="hand2", fg="white",
           bg="green", command=login).place(x=50, y=40, width=300)
    Label(root, text="").pack()

    Button(frame3, text='Exit', height="3", width="20", bd=8, font=('arial', 20, 'bold'), cursor="hand2", fg="white",
           bg="green", command=exitting).place(x=80, y=250, width=250)
    Label(root, text="").pack()


main_display()
mainloop()
