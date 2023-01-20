from tkinter import *
import tkinter.messagebox
import mysql.connector


myconn = mysql.connector.connect(host="localhost",user="root",passwd="", database="farm")
mycursor = myconn.cursor()


def Exit():
    wayOut = tkinter.messagebox.askyesno("Maendeleo Chapchap Farm", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return


def maize_details():
    showOut = tkinter.messagebox.showinfo("Wheat Section", "There are 10 Sacks of Wheat")
    print(showOut)


def beans_details():
    showOut = tkinter.messagebox.showinfo("Potatoes Section", "There are 20 Sacks of Potatoes")
    print(showOut)


def milk_details():
    showOut = tkinter.messagebox.showinfo("Tomatoes Section", "There are 30 grates of Tomatoes")
    print(showOut)


def meat_details():
    showOut = tkinter.messagebox.showinfo("Mangoes Section", "There are 20 sacks of Mangoes")
    print(showOut)


def skins_details():
    showOut = tkinter.messagebox.showinfo("Bananas Section", "There are 20 bananas")
    print(showOut)


def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Farm Management System")
    root.geometry("500x500")
    Label(root,text='Maendeleo Chapchap Farm',  font=('arial', 20, 'bold'), relief="groove", fg="red",
                   bg="yellow",width=300).pack()
    Label(root,text="").pack()
    Label(root,text='Products Available in Store', height="1",width="25",font=('arial', 20, 'bold'), relief="groove", fg="green",
                   bg="white").pack()
    Label(root,text="").pack()

    Button(root, text='Wheat', height="1", width="20",font=('arial', 12, 'bold'), relief="groove", fg="blue",
           bg="white", command=maize_details).place(x=20,y=150)

    Button(root, text='Potatoes', height="1", width="20",font=('arial', 12, 'bold'), relief="groove", fg="blue",
           bg="white", command=beans_details).place(x=270,y=150)

    Button(root, text='Tomatoes', height="1", width="20", font=('arial', 12, 'bold'), relief="groove", fg="blue",
           bg="white", command=milk_details).place(x=20,y=200)

    Button(root, text='Mangoes', height="1", width="20",font=('arial', 12, 'bold'), relief="groove", fg="blue",
           bg="white", command=meat_details).place(x=270,y=200)

    Button(root, text='Bananas', height="1", width="20", font=('arial', 12, 'bold'), relief="groove", fg="blue",
           bg="white", command=skins_details).place(x=20,y=250)

    Label(root, text='Click on the Item for its Details', height="1", width="25", font=('arial', 20, 'bold'), relief="groove",
          fg="black",
          bg="white").place(x=30, y=300)

    Button(root,text='Exit', height="1",width="20", font=('arial', 12, 'bold'), relief="groove", fg="red",
                   bg="yellow",command=Exit).place(x=150,y=350)
    Label(root,text="").pack()

main_display()
mainloop()
