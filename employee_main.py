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

#Selecting all of the columns from the database to display when the user tells us, 
# in both the crm_data table in a variable named my_result and the Mailings table in a variable named other_result.
my_result = my_db.executeSelectQuery("SELECT * FROM employee_data") 
#Creating a blank list
entire_employee_list = []
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
        #Testing for the employee date of hire.
        while not not_hire:
            dateOfHire = input("Please enter the employee date of hire: ")
            not_hire = my_employee.validateDateOfHire(dateOfHire)
        #Setting a flag.
        not_leave = False
        #Testing for the employee last name.
        while not not_leave:
            not_continue = input("Does the employee have a retirement date? Y/N: ")
            if not_continue.lower() == "y":

                dateOfLeave = input("Please enter the employee date of seperation: ")
                not_leave = my_employee.validateDateOfHire(dateOfLeave)
            elif not_continue.lower() == "n":
                break
            else:
                print(f"Sorry, but \'{not_continue}\' is not a valid option, please try again!")
        #Setting a flag.
        not_number = False
        #Testing for the employee number.
        while not not_number:
            employee_number = input("Please enter your employee number: ")
            not_number = my_employee.validateNumber(employee_number)
        #Setting a flag.
        not_phone = False
        #Testing for the employee phone number.
        while not not_phone:
            employee_phone = input("Please enter the employee primary phone number: ")
            not_phone = my_employee.validatePhone(employee_phone)
        #Setting a flag.
        not_second_phone = False
        #Testing for the employee phone number.
        while not not_second_phone:
            not_continue = input("Does the employee have a secondary phone number? Y/N: ")
            if not_continue.lower() == "y":
                employee_second_phone = input("Please enter the employee secondary number: ")
                not_phone = my_employee.validatePhone(employee_second_phone)
            elif not_continue.lower() == "n":
                not_second_phone = False
                break
            else:
                print(f"Sorry, but \'{not_continue}\' is not a valid option, please try again!")

        #Setting a flag.
        not_address = False
        #Testing for the employee address.
        while not not_address:
            employee_address = input("Please enter the employee address: ")
            not_address = my_employee.validateAddress(employee_address)
        if type(not_second_phone) is True:
            entire_employee_list.append({"Employee Name:":combined_name, "Employee Number:":employee_number,"Date of Hire":dateOfHire,"Date of leave":dateOfLeave,"Employee Phone number:":employee_phone,"Employee Secondary Phone:":employee_second_phone})
        
        #Need to add something if the employee seperated from the company.
        #So they have their own dictionary.
        
        else:
            entire_employee_list.append({"Employee Name:":combined_name, "Employee Number:":employee_number,"Date of Hire":dateOfHire,"Date of leave":dateOfLeave,"Employee Phone number:":employee_phone})

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
        combined_name+"\',\'"+dateOfHire +"\',\'"+ dateOfLeave +"\',\'"+employee_phone+"\',\'"+ employee_second_phone+"\',\'"+ employee_address+"\',\'"+ "\')")

    #Handing the case where the user selects option 7.
    elif decision.isdigit() == 7:
        employee_list = "text_files/employee_list.txt"
        print("Export an excel spreadsheet of the current employees...")
        with open (employee_list, 'r') as emp_list:
            print("Adding employees to a csv file...")

            with open("text_files/employee_list.csv","w+") as CSV_list:
                #Need to replace the list below with one that is populated already.
                for employee in emp_list:
                    #Adding each part of employee data to the csv list.
                    CSV_list.write(employee)