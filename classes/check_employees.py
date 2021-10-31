class Employee:
    """
    Created a class that represents the act
    of validating employees and adding them to a dictionary.
    """
    def __init__(self,employeename,employeenumber,employeeLengthOfService):
        """
        Initializing the following attributes:
        - employeename
        - employeenumber
        - employeeLengthOfService
        """
        self.employeename = employeename
        self.employeenumber = employeenumber
        self.employeeLengthOfService = employeeLengthOfService
    def addEmployee(self,employeeName):
        """
        Creating a method that will add an employee to a dictionary.
        """
    def checkNumber(self,Employeenumber):
        """
        Creating a method that will validate an employee number.
        """
        (("." in Employeenumber) and (Employeenumber.replace('.','')).isdigit() and len(Employeenumber) == 10)
    def validateDateOfHire(self,employeeDate):
        """
        Creating a method that will validate the date for when an 
        employee is hired or seperates from the company.
        """
        if (("." in employeeDate) and (employeeDate.replace('.','')).isdigit() and len(employeeDate) == 10) or (("-" in employeeDate) and (employeeDate.replace('-','')).isdigit() and len(employeeDate) == 10) or (employeeDate.isdigit() and len(employeeDate) == 8):
            return True
        else:
            return False
    def validateEmployee(self,employeeName):
        """
        Creating a method that will validate an employee's name.
        """
        if (("." in employeeName) and (employeeName.replace('.','')).isalpha() and len(employeeName) >= 1) or (("-" in employeeName) and (employeeName.replace('-','')).isalpha() and len(employeeName) >= 1) or (("'" in employeeName) and (employeeName.replace('\'','')).isalpha() and len(employeeName) >= 1) or (employeeName.isalpha() and len(employeeName) >= 1):
            return True
        else:
            return False