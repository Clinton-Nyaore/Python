from tkinter import *
top = Tk()
import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="amos")
my_cursor = my_db.cursor()

top.geometry('500x500')
top.maxsize(width=300, height=200)
top.minsize(width=300, height=200)
top.title('Amos Calculator')
top.configure(bg='green')

l = Label(top, text='Amos Calculator', fg='green').grid(row=0, column=1, sticky=W)
l1 = Label(top, text='First Number').grid(row=1, column=0, sticky=W)
l2 = Label(top, text='Second Number').grid(row=2, column=0, sticky=W)
l3 = Label(top, text='Operator').grid(row=3, column=0, sticky=W)
l4 = Label(top, text='Answer').grid(row=4, column=0, sticky=W)

E1 = Entry(top, bd=5)
E1.grid(row=1, column=1)
E2 = Entry(top, bd=5)
E2.grid(row=2, column=1)
E3 = Entry(top, bd=5)
E3.grid(row=3, column=1)
E4 = Entry(top, bd=5)
E4.grid(row=4, column=1)


def proces():
    global answer
    number1 = Entry.get(E1)
    number2 = Entry.get(E2)
    operator = Entry.get(E3)
    number1 = int(number1)
    number2 = int(number2)
    if operator == "+":
        answer = number1 + number2
    if operator == "-":
        answer = number1 - number2
    if operator == "*":
        answer = number1 * number2
    if operator == "/":
        answer = number1 / number2
    Entry.insert(E4, 0, answer)
    print(answer)

    sql = "INSERT INTO calci (what, answer) VALUES (%s, %s)"
    val = ("Answer", answer)
    my_cursor.execute(sql, val)

    my_db.commit()
    print(my_cursor.rowcount, "record inserted.")

B = Button(top, text="Submit", command=proces, bg='yellow').grid(row=5, column=1)

top.mainloop()
