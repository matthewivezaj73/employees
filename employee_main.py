#Importing modules.
from classes.check_employees import *
#Setting a flag.
not_employee = False
#Testing for adding employees.
while not not_employee:
    decision = input("1. Create an employee.\n2. Show Current employees.\n3. Show seperated employees.\n4. Edit an employee.\n5. Import to database.\n6. Export a excel spreadsheet")