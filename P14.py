# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:46:55 2026

"""
# Lisa Kraatz
# Ctr + 1 to comment out multiple lines quickly

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay): # Self needed in every method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        
        Employee.num_of_emps += 1 # using self doesn't make sense here (don't want it overwirtten for any one instance)
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount): #Class variable convention name cls
        cls.raise_amt = amount
    @classmethod # To add new employee from string instead of manually
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # Static method (don't depend on specific instance or class variable
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # 5 is Saturday, 6 is Sunday
            return False
        return True
        

# Define values
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Testing whether it's work day based on class method
import datetime
my_date = datetime.date(2025, 3, 19)
print(Employee.is_workday(my_date))

Employee.set_raise_amt(1.05) # using class method instead of instance method
# -> same as Employee.raise_amt = 1.05 


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# Creating new employee from string (Individually - we can do it with class mehod rather)
# first, last, pay = emp_str_1.split('-') #Split on -
# new_emp_1 = Employee(first, last, pay) # Instead of straight values, pass variables from split string

# With class method:
new_emp_1 = Employee.from_string(emp_str_1)

print(Employee.num_of_emps) # Returns number of declared instances after instantiation (2)

# Employee.raise_amount = 1.05 # Change value of class attribute for class and all instances
# emp_1.raise_amount = 1.05 # Only applies to that specific instance

print(emp_2.raise_amount)
# Both do the same thing:
print(emp_1.raise_amount)
print(Employee.raise_amount)
# -> Class variable accessable from class itself as well as both instances

# To print dictionary (Returns values with categories) 
# print(emp_1.__dict__) # Does not include class attributes UNLESS value changed for that instance

# print(Employee.__dict__) # Prints class attributes


print(emp_1.email)
# Both do the same thing:
print(emp_1.fullname())  # Need parentheses bc it's a method, not attribute
Employee.fullname(emp_1) # Similar to above statement but need to pass instance



# Use methods -> Instead of this (Manually): -------------
    
# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000

# To display first and last name use function inside class instead of this:
# print('{} {}'.format(emp_1.first, emp_1.last))
# ---------------------------------------------------------





