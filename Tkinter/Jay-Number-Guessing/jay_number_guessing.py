import tkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox

my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="jay")
my_cursor = my_db.cursor()


def exitting():
    way_out = tkinter.messagebox.askyesno("Jay's Number Guessing System", "Do you want to exit the system?")
    if way_out > 0:
        root.destroy()
        return


def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Jay's Number Guessing System")
    root.geometry("1280x800+0+0")

    global name
    global number

    name = StringVar()
    number = StringVar()

    frame1 = Frame(root, bg="pink")
    frame1.place(x=0, y=0, width=540, relheight=1)

    frame2 = Frame(root, bg="maroon")
    frame2.place(x=550, y=0, relwidth=1, relheight=1)

    Label(frame1, text="Jay's\nNumber\nGuessing\nSystem", font=("times new roman", 70, "bold"),
          bg="grey", fg="black").place(x=50, y=150)

    Label(frame2, text="<> Guess your Number Below <>", height="1", width="20",
          font=('arial', 20, 'bold'), cursor="hand2", fg="white", bg="black").place(x=10, y=90, width=450)

    Label(frame2, text="Your Name :", height="1", width="20",
          font=('arial', 20, 'bold'), cursor="hand2", fg="white", bg="black").place(x=100, y=150, width=250)
    Entry(frame2, textvariable=name).place(x=100, y=210, width=250, height=30)
    Label(frame2, text="").pack()

    Label(frame2, text="Tip !\nGuess a Number Between 1 & 10", height="3", width="20",
          font=('arial', 20, 'bold'), cursor="hand2", fg="red", bg="yellow").place(x=30, y=270, width=430)
    Label(frame2, text="").pack()

    Label(frame2, text="Your Guessed Number>>", height="1", width="20",
          font=('arial', 20, 'bold'), cursor="hand2", fg="white", bg="black").place(x=80, y=410, width=350)
    Entry(frame2, textvariable=number).place(x=180, y=470, width=100, height=35)
    Label(frame2, text="").pack()

    Button(frame2, text='Check', height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="green",
           bg="yellow", command=check_btn).place(x=100, y=520, width=250)
    Label(frame2, text="").pack()

    Button(frame2, text='Exit', height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
           bg="red", command=exitting).place(x=100, y=590, width=250)
    Label(frame2, text="").pack()


def check_btn():
    the_name = name.get()
    the_number = number.get()

    my_str = [the_name, the_number]

    if the_name == "" or the_number == "":
        messagebox.showinfo("Warning!", "Please input both fields!")

    else:
        my_cursor.execute("SELECT number FROM numbers")
        my_result = my_cursor.fetchall()
        for n in my_result:
            for a in n:
                if a == the_number:
                    messagebox.showinfo("Success", "Thanks {} for your participation\nYour Number is {} and it is Correct".format(my_str[0],my_str[1]))
                    break
                else:
                    messagebox.showinfo("Failure", "Thanks {} for your participation\nYour Number is {} and it is Wrong".format(my_str[0],my_str[1]))
                    break


main_display()
mainloop()
