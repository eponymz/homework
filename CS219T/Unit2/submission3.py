class Employee:
    def __init__(self, name, empID):
        self.name = name
        self.empID = empID
        self.salary = None

    def calcSalary(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Hourly(Employee):
    def __init__(self, name, empID):
        Employee.__init__(self, name, empID)
        self.hoursWorked = None
        self.payRate = None

    def calcSalary(self):
        self.hoursWorked = input("How many hours per week worked? ")
        self.payRate = input("Pay rate: ")
        self.salary = int(self.hoursWorked) * float(self.payRate) * 52


class Yearly(Employee):
    def __init__(self, name, empID):
        Employee.__init__(self, name, empID)
        self.years = None
        self.basePay = None

    def calcSalary(self):
        self.years = input("How many years has this employee worked at the company? ")
        self.basePay = input("Base pay: ")
        self.salary = int(self.basePay) + (int(self.basePay) * .10 * int(self.years))


employees = list()
empType = raw_input('Is the employee hourly or yearly? ')
if empType == 'hourly':
    empName = raw_input('What is the employee name? ')
    empID = raw_input('Whats the employeeID? ')
    employees.append(Hourly(empName, empID))
elif empType == 'yearly':
    empName = raw_input('What is the employee name? ')
    empID = raw_input('Whats the employeeID? ')
    employees.append(Yearly(empName, empID))
else:
    print 'You must pick yearly or hourly. Please restart program..'

for emp in employees:
    emp.calcSalary()

    print emp.name + " has a salary of " + str(emp.salary) + " per year."
