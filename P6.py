# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:01:52 2026

"""
# Lisa Kraatz

answer = 'y'

while (answer == 'y' or answer == 'Y'):
    minutes = 0
    runMin = input('\nEnter running minutes: ')
    print('------------\n')
    if (runMin.isnumeric()):
        runMin = float(runMin)
        if (runMin <= 5):
            message = '\nMinutes cannot be less than 5 or a negative number.'
            print('Running minutes entered:', runMin, message)
        else:
            print('Running minutes entered:', runMin,'\n')
            while(runMin- 4 > minutes):
                minutes += 5
                calories = minutes * 3.44
                print('Minutes:', minutes, ' Calories:', calories)

    else:
        message = '\nMinutes cannot be empty or contain letters.'
        print('Running minutes entered:', runMin, message)
        
    answer = input('\nRun again? (y/n): ')
    
print('\nLoop ended.')

