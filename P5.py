# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 09:54:09 2026

"""
# Lisa Kraatz

print('-----------')
print('\nOptions: add, subtract, multiply, divide\n')
print('-----------')

# Ask for operator
operator = input('Enter table action: ')

tableCode = ''
validityOp = ''

if(operator == 'add'):
   tableCode = 'A'
   validityOp = 'valid'
elif(operator == 'subtract'):
       tableCode = 'S'
       validityOp = 'valid'
elif(operator == 'multiply'):
        tableCode = 'M'
        validityOp = 'valid'
elif(operator == 'divide'):
        tableCode = 'D'
        validityOp = 'valid'
else:
    print('Input inavlid. Please enter "add", "subtract", "multiply" or "divide".\n')
    validityOp = 'invalid'

# Ask for number
x = input('Enter number: ')
xlengh = len(x)
validityNum = ''


if(x.isalpha()):
    print('Number cannot contain letters.')
    validityNum = 'invalid'
elif(x.isspace() or xlengh < 0):
    print('Number cannot be empty.')
    validityNum = 'invalid'
else:
    x = float(x)
    validityNum = 'valid'

# Display message
print('-----------')
print('\nSelected table code:',tableCode,'\nEntered number:',x,'\n',operator,'\n')

# Calculation

if(validityNum == 'valid' and validityOp == 'valid'):
    for i in range(1,11,1):
        if(tableCode == 'A'):
            calculation = x + i
            print(calculation, ' = ', x, ' + ', i )
        elif(tableCode == 'S'):
            calculation = x - i
            print(calculation, ' = ', x, ' - ', i )
        elif(tableCode == 'M'):
            calculation = x * i
            print(calculation, ' = ', x, ' * ', i )
        elif(tableCode == 'D'):
            calculation = x / i
            print(calculation, ' = ', x, ' / ', i )
elif(validityNum == 'invalid' or validityOp == 'invalid'):
    print('Calculation cannot be made because of invalid input.')
        
        
print('\n---Done')
        

        
 





