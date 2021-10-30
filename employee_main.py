#Importing modules.
from classes.check_employees import *
#Setting a flag.
not_employee = False
#Testing for adding employees.
while not not_employee:
    #Asking the user what they would like to do.
    decision = input("1. Create an employee.\n2. Show Current employees.\n3. Show seperated employees.\n4. Edit an employee.\n5. Import to database.\n6. Export a excel spreadsheet")
    #Handing the case where the user selects option 1.
    if decision.isdigit() == 1:
    #Handing the case where the user selects option 1.
    elif decision.isdigit() == 2:
    #Handing the case where the user selects option 1.
    elif decision.isdigit() == 3:
