#Importing modules.
from classes.check_employees import *
#Setting a flag.
not_employee = False
#Testing for adding employees.
while not not_employee:
    #Asking the user what they would like to do.
    decision = input("1. Create an employee.\n2. Show Current employees.\n3. Show seperated employees.\n4. Show all employees.\n5. Edit an employee.\n6. Import to database.\n7. Export a excel spreadsheet")
    #Handing the case where the user selects option 1.
    if decision.isdigit() == 1:
        print("Starting the process of creating the employee...")
    #Handing the case where the user selects option 2.
    elif decision.isdigit() == 2:
        print("Showing the current employees...")
    #Handing the case where the user selects option 3.
    elif decision.isdigit() == 3:
        print("Showing the seperated employees...")
    #Handing the case where the user selects option 4.
    elif decision.isdigit() == 4:
        print("Showing all employees...")
    #Handing the case where the user selects option 5.
    elif decision.isdigit() == 5:
        print("Begin editing employees...")
    #Handing the case where the user selects option 6.
    elif decision.isdigit() == 6:
        print("Begin Import employees to the database...")
