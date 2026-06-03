# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:35:37 2026

"""
# Lisa Kraatz

import random

# Declare Lists
powerBallList = []
megaMillionList = []
luckyDayList = []
lottoList = []

# Create lists
def createList():
    # Power Ball List
    for i in range(1,70,1):
        powerBallList.append(i)
    
    # Mega Million List
    for i in range(1,71,1):
        megaMillionList.append(i)
    
    # Lucky Day List
    for i in range(1,46,1):
        luckyDayList.append(i)
    
    # Lotto List
    for i in range(1,53,1):
        lottoList.append(i)
        
# Menu
def menu():
    ans = ''
    while (ans == ''):
        print('MENU------------------------------------------------')
        print('1. Powerball')
        print('2. Mega Million')
        print('3. Lucky Day lotto')
        print('4. Lotto')
        print('\n')
        print('9. Quit')
        print('-----------')
        selection = input('Select a lottery game: ')
        if(selection == '1'):
            powerBall()
            ans = input('Hit enter key to return to menu.\n')
        elif(selection == '2'):
            megaMillion()
            ans = input('Hit enter key to return to menu.\n')
        elif(selection == '3'):
            luckyDay()
            ans = input('Hit enter key to return to menu.\n')
        elif(selection == '4'):
            lotto()
            ans = input('Hit enter key to return to menu.\n')
        elif(selection == '9'):
            ans = 'x'
        else:
            print('Invalid input. Please enter only 1, 2, 3, 4 or 9.')
        print('--------------\n')
    print('\nProgram done.')

# Random numbers for each game
def powerBall():
    numbers = random.sample(powerBallList,5)
    numbers.sort()
    print('\n')
    print('Powerball numbers: ')
    print(*numbers,'\n')
    
def megaMillion():
    numbers = random.sample(megaMillionList,5)
    numbers.sort()
    print('\n')
    print('Mega Million numbers: ')
    print(*numbers,'\n')

def luckyDay():
    numbers = random.sample(luckyDayList,5)
    numbers.sort()
    print('\n')
    print('Lucky Day numbers: ')
    print(*numbers,'\n')
    
def lotto():
    numbers = random.sample(lottoList,6)
    numbers.sort()
    print('\n')
    print('Lotto numbers: ')
    print(*numbers,'\n')
    
# Main function
def main():
    createList()
    menu()


# Main    
main()



