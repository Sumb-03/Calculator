from tkinter import *

# Window

window = Tk()
window.title('Calculator')
window.geometry('328x460')
window.iconphoto(False, PhotoImage(file='C:/Users/User/Desktop/calculator.png'))

# Screen

screen = Entry(window, width=30, borderwidth=10)
screen.grid(column=1, row=0, columnspan=3)

# Calculations

def button_enter(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))

def button_clear():
    screen.delete(0, END)

def button_add():
    first_number = screen.get()
    global firstnumber
    global calculations
    calculations = 'addition'
    firstnumber = float(first_number)
    screen.delete(0, END)

def button_subtract():
    first_number = screen.get()
    global firstnumber
    global calculations
    calculations = 'subtraction'
    firstnumber = float(first_number)
    screen.delete(0, END)


def button_multiply():
    first_number = screen.get()
    global firstnumber
    global calculations
    calculations = 'multiplication'
    firstnumber = float(first_number)
    screen.delete(0, END)


def button_divide():
    first_number = screen.get()
    global firstnumber
    global calculations
    calculations = 'division'
    firstnumber = float(first_number)
    screen.delete(0, END)

def button_equal():
    screen_number = screen.get()
    screen.delete(0, END)
    if calculations == 'addition':
        screen.insert(0, firstnumber + float(screen_number))
    elif calculations == 'subtraction':
        screen.insert(0, firstnumber - float(screen_number))
    elif calculations == 'multiplication':
        screen.insert(0, firstnumber * float(screen_number))
    elif calculations == 'division':
        screen.insert(0, firstnumber / float(screen_number))

# Buttons

number0 = Button(window, height=5, width=9, text='0', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter(0))

number1 = Button(window, height=5, width=9, text='1', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter(1))
number2 = Button(window, height=5, width=9, text='2', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter(2))
number3 = Button(window, height=5, width=9, text='3', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter(3))

number4 = Button(window, height=5, width=9, text='4', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter(4))
number5 = Button(window, height=5, width=9, text='5', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter(5))
number6 = Button(window, height=5, width=9, text='6', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter(6))

number7 = Button(window, height=5, width=9, text='7', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter(7))
number8 = Button(window, height=5, width=9, text='8', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter(8))
number9 = Button(window, height=5, width=9, text='9', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter(9))

operator_divide = Button(window, height=5, width=9, text='/', font=('Arial', 10, 'bold'), bg='light grey', command=button_divide)
operator_multiply = Button(window, height=5, width=9, text='*', font=('Arial', 10, 'bold'), bg='light grey', command=button_multiply)
operator_subtract = Button(window, height=5, width=9, text='-', font=('Arial', 10, 'bold'), bg='light grey', command=button_subtract)
operator_add = Button(window, height=5, width=9, text='+', font=('Arial', 10, 'bold'), bg='light grey', command=button_add)
operator_equal = Button(window, height=5, width=9, text='=', font=('Arial', 10, 'bold'), bg='light blue', command=button_equal)

dot = Button(window, height=5, width=9, text='.', font=('Arial', 10, 'bold'), bg='white', command=lambda: button_enter('.'))
clear = Button(window, height=5, width=9, text='C', font=('Arial', 10, 'bold'), bg='white', command=button_clear)

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

operator_divide.grid(column=4, row=1)
operator_multiply.grid(column=4, row=2)
operator_subtract.grid(column=4, row=3)
operator_add.grid(column=4, row=4)
operator_equal.grid(column=4, row=0)

dot.grid(column=3, row=4)
clear.grid(column=1, row=4)


window.mainloop()
