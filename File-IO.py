# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:06:53 2026

"""
# Lisa Kraatz

# Imports
from datetime import datetime

# Time Stamp
timestamp = datetime.now()

# Input File
try:
    inputFile = 'E:/Private/School/CIS- 103/Assignments/P11/P11.txt'
    starterFile = open(inputFile, 'r')
except:
    print('File open error.')

# Define functions
def process():
    points = 0 
    message = ''
    grade = ''
    recordCount = 0
    goodRecords = 0
    badRecords = 0
    aCount = 0
    bCount = 0
    cCount = 0
    dCount = 0
    fCount = 0
    idNum = 0
    name = ''
#  Output Files
    outputFile1 = 'E:/Private/School/CIS- 103/Assignments/P11/grades.txt'
    gradeFile = open(outputFile1, 'w')
    outputFile2 = 'E:/Private/School/CIS- 103/Assignments/P11/errors.txt'
    errorFile = open(outputFile2, 'w')
# Read records
    line = starterFile.readline()
    while(line != ''):
        recordCount += 1
        (idNum,name,points) = line.split(',')
# Remove spaces
        idNum = idNum.strip()
        name = name.strip()
        points = points.strip()
# Catch value errors
        try:
            pointsFloat = float(points)
        except:
            message = 'Points are not a number.'
            badRecords += 1
            errorFile.write(idNum+ ', '+name+', '+ str(pointsFloat)+ ', '+ message+'\n')
            line = starterFile.readline()
            continue
# Validate range and output
        if(pointsFloat <0 or pointsFloat >1000):
            message = 'Points are not between 0 and 1000'
            badRecords += 1
            pointsFloat = str(points)
            errorFile.write(idNum+ ', '+name+', '+ str(pointsFloat)+ ', '+ message+'\n')
        elif (pointsFloat >= 900 and pointsFloat <= 1000):
            grade = 'A'
            aCount += 1
            goodRecords += 1
            gradeFile.write(idNum+ ', '+name+', '+ str(pointsFloat)+ ', '+ grade+'\n')
        elif (pointsFloat >= 800 and pointsFloat <= 899):
            grade = 'B'
            bCount += 1
            goodRecords += 1
            gradeFile.write(idNum+ ', '+name+', '+ str(pointsFloat)+ ', '+ grade+'\n')
        elif (pointsFloat >= 700 and pointsFloat <= 799):
            grade = 'C'
            cCount += 1
            goodRecords += 1
            gradeFile.write(idNum+ ', '+name+', '+ str(pointsFloat)+ ', '+ grade+'\n')
        elif (pointsFloat >= 600 and pointsFloat <= 699):
            grade = 'D'
            dCount += 1
            goodRecords += 1
            gradeFile.write(idNum+ ', '+name+', '+ str(pointsFloat)+ ', '+ grade+'\n')
        elif (pointsFloat >= 0 and pointsFloat <= 599):
            grade = 'F'
            fCount += 1
            goodRecords += 1
            gradeFile.write(idNum+ ', '+name+', '+ str(pointsFloat)+ ', '+ grade+'\n')
        line = starterFile.readline()
    starterFile.close()
    gradeFile.close()
    errorFile.close()
    return recordCount, badRecords, goodRecords, aCount, bCount, cCount, dCount, fCount
    

def main():
    print('Start of Program: ',timestamp,'\n')
    recordCount, badRecords, goodRecords, aCount, bCount, cCount, dCount, fCount = process()
    print('Number of records read: ', recordCount,'\n')
    print('Number of good records to grade file: ', goodRecords)
    print('Number of bad records to error file: ', badRecords,'\n')
    print('Number of A\'s:', aCount)
    print('Number of B\'s:', bCount)
    print('Number of C\'s:', cCount)
    print('Number of D\'s:', dCount)
    print('Number of F\'s:', fCount,'\n')
    print('End of Program: ',timestamp)
    

# Main
main()
