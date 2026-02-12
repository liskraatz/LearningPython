# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:50:19 2026

"""

# Lisa Kraatz

# Get name 
name = input('Enter a name: ')

nameLen = len(name)

if (nameLen == 0 or name.isspace()):
    print('Name cannot be empty.\n')
    nMessage = 'invalid'
else:
    if(name.isnumeric()):
        print('Name cannot contain a number.\n')
        nMessage = 'invalid'
    else:
        if(nameLen <3):
            print('Name has to be at least 3 characters long.\n')
            nMessage = 'invalid'
        else:
            print('Name is valid.\n')
            nMessage = 'valid'
            
# Get Account number
accNum = input('Enter Account number: ')
accNumLen = len(accNum)
 
if(accNum.isalpha()):
    print('Account number cannot contain alphabetic characters.\n')
    anMessage = 'invalid'
else:
    if(accNum.isspace()):
        print('Account number cannot be empty or contain spaces.\n')
        anMessage = 'invalid'
    else:
        if(accNumLen != 9):
             print('Account number has to have 9 digits.\n')
             anMessage = 'invalid'
        else:
             print('Account number valid.\n')
             accNum = int(accNum)
             anMessage = 'valid'

# Get Payment amount
payAmount = input('Enter Payment amount: ')
payAmountLen = len(payAmount)
 
if(payAmount.isspace() or payAmountLen == 0):
     print('Payment amount cannot be empty.\n')
     paMessage = 'invalid'
else:
     if(payAmount.isalpha()):
         print('Payment amount cannot contain alphabetic characters.\n')
         paMessage = 'invalid'
     else:
         payAmount = float(payAmount)
         if(payAmount <=0):
             print('Payment amount cannot be zero or a negative number.\n')
             paMessage = 'invalid'
         else:
             print('Payment amount is valid.\n')
             paMessage = 'valid'

# Display results


print('Name:', name, nMessage,'\nAccount number:', accNum, anMessage,'\nPayment: $',payAmount, paMessage)
                                
                            
                    
                





        

