# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:07:52 2026

"""
# Lisa Kraatz

def calculation(n):
    if n == 1:
        return n
    else:
        return (n*(n+1))/2
            

def main():
    ans = 'y'
    while ans.lower() == 'y':
        print('\n--Sum of numbers--')
        numb = input('Enter a number: ')
        try:
            numb = int(numb)
            if (numb < 0):
                print('Number cannot be negative.')
            else:
                result = int(calculation(numb))
                for i in range (numb,1,-1):
                    print(i,'+ ',end = '')
                print('1 =',result,end = '')
                print('\n')
        except:
            print('Invalid input detected.')
        ans = input('\nAnother number? (y/n) ')
    print('\nProgram done :)')
    
# Main
main()
    
