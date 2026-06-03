# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 10:10:12 2026

@author: Moonl
"""

# Lisa Kraatz

import math

# Area of rectangle: A = w * h

print('------------')
print('Area of Rectangle')
print('------------')
print('\n')
widthRect = int(input('Type in width: '))
heightRect = int(input('Type in height: '))

resultRect = widthRect * heightRect
print('The area of the rectangle is: ', resultRect) 

print('\n')

# Area of triangle: A = 1/2b b * h

print('------------')
print('Area of Triangle')
print('------------')
print('\n')
baseTri = int(input('Type in base: '))
heightTri = int(input('Type in height: '))

resultTri = (baseTri * heightTri) / 2
print('The area of the triangle is: ', resultTri) 

print('\n')

# Area of circle: A = pi * r^2

print('------------')
print('Area of Circle')
print('------------')
print('\n')
radius = int(input('Type in radius: '))

resultCirc = math.pi * math.pow (radius,2)
print('The area of the Circle is: ', resultCirc) 

print('\n')
