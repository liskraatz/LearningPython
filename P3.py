# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 10:14:10 2026

@author: Moonl
"""

#Lisa Kraatz


screwPound = float(input('Enter pounds of screws to be purchased: '))

if (screwPound <= 0):
    print('Please enter a number greater than 0.')
else:
    print('You entered ', screwPound, 'pounds to be purchased.')
    

poundPrice = 0.99
gross = screwPound * poundPrice
discount = ''

if (screwPound >= 10) and (screwPound <= 99.99):
    discount = 0.10
elif (screwPound >=100 and screwPound <= 999.99):
    discount = 0.20
elif (screwPound >=1000 and screwPound <= 9999.99):
    discount = 0.3
elif (screwPound >= 10000):
    discount = 0.4
else:
    discount = 0

discountAmount = gross * discount
final = gross - discountAmount

print('\n'*3)
print('Number of pounds purchased:', screwPound, '\nGross sales:', '$' ,gross, '\nDiscount amount:', '$' ,discountAmount, '\nFinal Amount:', '$' ,final,)

