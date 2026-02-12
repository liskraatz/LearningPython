# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 10:21:59 2026

@author: Moonl
"""

# Lisa Kraatz

fName = input('Enter first name: \n')
lName = input('Enter last name: \n')
street = input('Enter street address: \n')
city = input('Enter city: ')
state = input('Enter state code (Format: XX): ')
zipCode = input('Enter zip code: ')

name = fName + ' ' + lName
address = street + '\n' + city + ',' + ' ' + state + ' ' + zipCode

print('\n')
print(name + '\n' + address)