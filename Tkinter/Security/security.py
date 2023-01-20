import tkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox

my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="security")
my_cursor = my_db.cursor()


def exitting():
    way_out = tkinter.messagebox.askyesno("Exit", "Do you want to exit the system?")
    if way_out > 0:
        root.destroy()
        return


def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("The Ranges Security")
    root.geometry("1280x800+0+0")

    global name
    global phone
    global tin
    global tout

    name = StringVar()
    phone = StringVar()
    tin = StringVar()
    tout = StringVar()

    frame1 = Frame(root, bg="blue")
    frame1.place(x=0, y=0, width=550, relheight=1)

    frame2 = Frame(root, bg="grey")
    frame2.place(x=550, y=0, relwidth=1, relheight=1)

    Label(frame1, text="The\nRanges\n Security", font=("times new roman", 70, "bold"), bg="blue", fg="white").place(x=40,
                                                                                                            y=150)



    Label(frame2, text=":: Enter your details here ::", height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2",
          fg="white",
          bg="blue").place(x=90, y=50, width=350)

    Label(frame2, text="Your Name :", height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
          bg="gray").place(x=150, y=110, width=250)
    Entry(frame2, textvariable=name).place(x=150, y=170, width=250, height=30)
    Label(frame2, text="").pack()

    Label(frame2, text="Your Phone Number :", height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
          bg="gray").place(x=150, y=210, width=290)
    Entry(frame2, textvariable=phone).place(x=150, y=270, width=250, height=30)
    Label(frame2, text="").pack()

    Label(frame2, text="Time In :", height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
          bg="gray").place(x=150, y=310, width=250)
    Entry(frame2, textvariable=tin).place(x=150, y=370, width=250, height=35)
    Label(frame2, text="").pack()

    Label(frame2, text="Time Out:", height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
          bg="gray").place(x=150, y=410, width=310)
    Entry(frame2, textvariable=tout).place(x=150, y=470, width=250, height=35)
    Label(frame2, text="").pack()

    Button(frame2, text='Submit', height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
           bg="blue", command=submit_btn).place(x=150, y=530, width=250)
    Label(frame2, text="").pack()

    Button(frame2, text='Exit', height="1", width="20", font=('arial', 20, 'bold'), cursor="hand2", fg="white",
           bg="red", command=exitting).place(x=180, y=600, width=200)
    Label(frame2, text="").pack()


def submit_btn():
    the_name = name.get()
    the_phone = phone.get()
    the_tin = tin.get()
    the_tout = tout.get()

    my_str = [the_name, the_phone, the_tin, the_tout]

    if the_name == "" or the_phone == "" or the_tin == "" or the_tout == "":
        messagebox.showinfo("Warning!", "Please input all values!")

    else:
        sql = """INSERT INTO details(name, phone, tin, tout) 
                VALUES("%s", "%s", "%s", "%s")"""
        val = (my_str[0], my_str[1], my_str[2], my_str[3])
        my_cursor.execute(sql, val)

        my_db.commit()
        messagebox.showinfo("Success", f"""Welcome {my_str[0]} and feel secure with our security""")



main_display()
mainloop()
