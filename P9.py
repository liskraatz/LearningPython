# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 10:01:35 2026

"""
# Lisa Kraatz

acres = 0
quarts = 0
fahrenheit = 0

hect = 0
l = 0 
k = 0


# Defining Functions

def hectares():
    acres = input('Enter acres: ')
    try:
        acres = float(acres)
        if(acres > 0):
            hect =  acres * 0.4047
        else:
            hect = 'Acres have to be greater than zero.'
        print(acres,'acres converts to', hect,'hectares')
    except:
        print('Input Error - Acres')
    return

def liters():
    quarts = input('Enter quarts: ')
    try:
        quarts = float(quarts)
        if (quarts > 0):
            l = quarts * 0.946353
        else:
            l = 'Quarts have to be greater than zero.'
        print(quarts,'quarts converts to', l,'liters')
    except:
        print('Input Error - Quarts')
    return
    
def kelvin():
    fahrenheit = input('Enter fahrenheit: ')
    try:
        fahrenheit = float(fahrenheit)
        k = (fahrenheit-32) * (5/9) + 273.15
        print(fahrenheit,'fahrenheit converrts to', k,'kelvin')
    except:
        print('Input Error - Fahrenheit')
    return

def main():
    ans = 'y'
    while (ans == 'y'):
        print('\nCoversion Program\n')
        hectares()
        print('\n----------\n')
        liters()
        print('\n----------\n')
        kelvin()
        print('\n----------\n')
        ans = input('Run again? y/n ')
    print('\n-----Program done-----')
    return

# Main

main()    
    
     

