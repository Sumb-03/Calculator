from tkinter import *

# Window
window = Tk()
window.title('Basic Calculator')
window.geometry('328x460')

# Screen

screen = Entry(window, width=30, borderwidth=10)
screen.grid(column=1, row=0, columnspan=3)

# Buttons
number0 = Button(window, height=5, width=9, text='0', font=('Arial', 10))
number1 = Button(window, height=5, width=9, text='1', font=('Arial', 10))
number2 = Button(window, height=5, width=9, text='2', font=('Arial', 10))
number3 = Button(window, height=5, width=9, text='3', font=('Arial', 10))
number4 = Button(window, height=5, width=9, text='4', font=('Arial', 10))
number5 = Button(window, height=5, width=9, text='5', font=('Arial', 10))
number6 = Button(window, height=5, width=9, text='6', font=('Arial', 10))
number7 = Button(window, height=5, width=9, text='7', font=('Arial', 10))
number8 = Button(window, height=5, width=9, text='8', font=('Arial', 10))
number9 = Button(window, height=5, width=9, text='9', font=('Arial', 10))
operator1 = Button(window, height=5, width=9, text='/', font=('Arial', 10))
operator2 = Button(window, height=5, width=9, text='*', font=('Arial', 10))
operator3 = Button(window, height=5, width=9, text='-', font=('Arial', 10))
operator4 = Button(window, height=5, width=9, text='+', font=('Arial', 10))
dot = Button(window, height=5, width=9, text='.', font=('Arial', 10))
operator5 = Button(window, height=5, width=9, text='=', font=('Arial', 10))

# Grid
number0.grid(column=2, row=4)
number1.grid(column=1, row=3)
number2.grid(column=2, row=3)
number3.grid(column=3, row=3)
number4.grid(column=1, row=2)
number5.grid(column=2, row=2)
number6.grid(column=3, row=2)
number7.grid(column=1, row=1)
number8.grid(column=2, row=1)
number9.grid(column=3, row=1)
operator1.grid(column=4, row=1)
operator2.grid(column=4, row=2)
operator3.grid(column=4, row=3)
operator4.grid(column=4, row=4)
operator5.grid(column=4, row=0)
dot.grid(column=3, row=4)





window.mainloop()
