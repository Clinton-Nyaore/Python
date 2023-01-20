from tkinter import *
from tkinter import messagebox
import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="ntsa")
my_cursor = my_db.cursor()


def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Police Brutality System")
    root.geometry("500x500")

    global  complaint, complainant
    complaint = str()
    complainant = str()

    Label(root, text="Police Brutality Cases", fg="black", font=('arial', 12, 'bold')).pack()
    Label(root, text="").pack()

    Label(root, text="Complainant :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=complainant).pack()
    Label(root, text="").pack()


    Label(root, text="Complaint :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=complaint).pack()
    Label(root, text="").pack()

    Button(root, text="Submit", bg="green", fg='white', relief="groove",
           font=('arial', 12, 'bold'), command=logged).pack()
    Label(root, text="").pack()

    Button(root, text='Exit', height="1", width="20",font=('arial', 12, 'bold'), cursor="hand2", fg="red",
           bg="green", command=exitting).pack()
    Label(root, text="").pack()


def complaint_destroy():
    the_complaint.destroy()
    root.destroy()


def logged():
    my_cursor.execute("SELECT * FROM cases")
    my_result = my_cursor.fetchall()
    global x
    for x in my_result:
        x += x

    global the_complaint
    the_complaint = Toplevel(root)
    the_complaint.title("Welcome")
    the_complaint.geometry("500x150")
    Label(the_complaint, text="""Welcome {} 
     to Police Brutality System,\n your complaint is \n<<{}>>""".format(x[1], x[2]), fg="blue",
          font="bold").pack()
    Label(the_complaint, text="").pack()
    Button(the_complaint, text="Logout", bg="green", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=complaint_destroy).pack()


def exitting():
    way_out = messagebox.askyesno("Police Brutality System", "Do you want to exit the system?Hope you were assisted!")
    if way_out > 0:
        root.destroy()
        return


main_display()
mainloop()
