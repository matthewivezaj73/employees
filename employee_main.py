#Import libraries.
import json
import os
import shutil
import time

#Importing modules.
from classes.check_employees import *
from classes.database_access import *

#Creating an instance of the employee class.
my_employee = Employee("Sam",424214,"11-30-2018")

#Creating a connection to the database
my_db = DB_Connect('root','','python_projects')

#Selecting all of the columns from the database to display when the user tells us, in both the crm_data table in a variable named my_result and the Mailings table in a variable named other_result.
my_result = my_db.executeSelectQuery("SELECT * FROM employee_data") 


#Setting a flag.
not_employee = False
#Testing for adding employees.
while not not_employee:
    #Asking the user what they would like to do.
    decision = input("Select a corresponding number to make your decision.\n1. Create an employee.\n2. Show Current employees.\n3. Show seperated employees.\n4. Show all employees.\n5. Edit an employee.\n6. Import to database.\n7. Export an excel spreadsheet: ")
    #Handing the case where the user selects option 1.
    if decision.isdigit() == 1:
        print("Starting the process of creating the employee...")
        not_first_name = False
        #Testing for the employee first name.
        while not not_first_name:
            f_name = input("Please input your first name: ")
            not_first_name = my_employee.validateEmployee(f_name)
        #Setting a flag
        not_last_name = False
        #Testing for the employee last name.
        while not not_last_name:
            l_name = input("Please input your last name: ")
            not_last_name = my_employee.validateEmployee(l_name)
        #Combining the first name and last name together to for proper entry into phpmyadmin.
        combined_name = f"{f_name} {l_name}"
        #Setting a flag.
        not_hire = False
        while not not_hire:
            dateOfHire = input("Please enter the employee date of hire: ")
            not_hire = my_employee.validateDateOfHire(dateOfHire)
        dateOfLeave = input("Please enter the employee date of seperation: ")
        employee_number = input("Please enter your employee number: ")
    #Handing the case where the user selects option 2.
    elif decision.isdigit() == 2:
        print("Showing the current employees...")
        for result in my_result:
            print(result)
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
        my_db.executeQuery("INSERT INTO crm_data (employee_name, date_of_hire, date_of_seperation, employee_phone, employee_secondary_phone,employee_address) VALUES (\'"+
        combined_name+"\',\'"+dataOfHire +"\',\'"+ city_information_value +"\',\'"+state.upper()+"\',\'"+ zip_code_value+"\',\'"+ company+"\',\'"+ 
        primary_phone_number_value+"\',\'"+ secondary_phone_number_value+"\',\'"+ email_address_value+"\')")

    #Handing the case where the user selects option 7.
    elif decision.isdigit() == 7:
        print("Export an excel spreadsheet of the current employees...")
