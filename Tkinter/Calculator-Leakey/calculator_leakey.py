from tkinter import *
top = Tk()


top.geometry('500x500')
top.maxsize(width=300, height=200)
top.minsize(width=300, height=200)
top.title('Calculator')
top.configure(bg='red')

label = Label(top, text='Leakey Calculator', fg='red').grid(row=0, column=1, sticky=W)


def speech_converter():
    print('Welcome')


button = Button(top, text="Submit", command=speech_converter, bg='yellow').grid(row=5, column=1,)

top.mainloop()
