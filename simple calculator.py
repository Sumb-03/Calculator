import os
import sys

# Numbers and Operations
first_number = input('Enter the first number: ')
operator = input('\nOperator: ')
second_number = input('\nEnter the second number: ')

first_number = float(first_number)
second_number = float(second_number)

# Calculations
if operator == '+':
    print('\nAnswer: ' + str(first_number + second_number))
elif operator == '-':
    print('\nAnswer: ' + str(first_number - second_number))
elif operator == '*':
    print('\nAnswer: ' + str(first_number * second_number))
elif operator == '/':
    print('\nAnswer: ' + str(first_number / second_number))
else:
    print('\nError: Invalid Operator')

# Try again
answer = input('\nTry Again? (y/n): ')
if answer == 'y':
    os.startfile(__file__)
    sys.exit()
elif answer == 'n':
    input('\nPress Any Key to Exit')
