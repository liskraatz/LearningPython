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
        

# Subclass of Employee
class Developer(Employee):
    raise_amt = 1.10 # Change raise amount from Employee class just for sublass
    def __init__(self, first, last, pay, prog_lang): # Used to add another variable just for subclass
        super().__init__(first, last, pay) # Gets these from super class, so we don't have to give it again
        # Or Employee.__init__(self, first, last, pay) # Does same thing as above line
        self.prog_lang = prog_lang
        
# Another subclass
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None): # Instead of initializing empty list here (bad practice)
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        
    
dev_1 = Developer('Corey', 'Schafer', 50000,'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2) # Adds employee to list
mgr_1.remove_emp(dev_1) # Removes employee from list
mgr_1.print_emps() # Prints list of employess that manager supervises

print(isinstance(mgr_1, Manager)) # <- Returns true or false for whether mgr_1 is an instance of Manager class
print(issubclass(Developer, Employee)) # <- Returns true or false for whether Developer is a subclass of Employee


# print(help(Developer)) <-- Shows how python handled the subclass

# print(dev_1.email)
# print(dev_1.prog_lang)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()






