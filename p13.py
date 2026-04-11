# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:59:17 2026

"""
# Lisa Kraatz

def dictionary():
    romanDt = {
        1:'I',
        2:'II',    
        3:'III',
        4:'IV',
        5:'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X',
        11: 'XI',
        12: 'XII',
        13: 'XIII',
        14: 'XIV',
        15: 'XV',
        16: 'XVI',
        17: 'XVII',
        18: 'XVIII',
        19: 'XIX',
        20: 'XX',
        21: 'XXI',
        22: 'XXII',
        23: 'XXIII',
        24: 'XXIV'
        }
    
    print('\nDictionary - integers to roman numerals\n\n', romanDt)
    ans = 'y'
    while (ans.lower() == 'y'):
        number = input('\nEnter number to be translated: ')
        try:
            number = int(number)
            while (number >0):
                if (number in romanDt):
                    translation = romanDt[number]
                    print(number,'in roman alphabet =',translation,'\n')
                elif(number not in romanDt):
                    print('Number not yet in dictionary.')
                    addQuestion = input('Add to dictionary? y/n: ')
                    if (addQuestion.lower() == 'y'):
                        print('For', number)
                        newRoman = input('Enter roman numeral: ')
                        if (newRoman.isalpha()):
                            newRoman = newRoman.upper()
                            romanDt[number] = newRoman
                            print('\n--New entry has been added--')
                            print(number,'in roman alphabet =',newRoman)
                        else:
                            print('Input invalid.')
                    else: 
                        print('Nothing added to dictionary.\n')
                number = int(input('Enter new number: '))
        except:
            print('\nNumber can\'t be translated because of invalid input.')
            
        ans = input('Translation ended. Run again? y/n: ')
    
    print('\n--Program done--\n')
    for entries in romanDt:
        print('Integer:',entries, 'Translation:',romanDt[entries])
       

#Main
dictionary()







