from tkinter import *
base = Tk()
myLabel = Label(base , text="User Name :")
myLabel_1 = Label(base , text="Password :")
myButton = Button(base , text="Submit")
myLabel.grid(row=0,column=0)
myLabel_1.grid(row=1,column=0)
myButton.grid(row=2,column=0)

e1=Entry()
e2=Entry()
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
base.mainloop()
