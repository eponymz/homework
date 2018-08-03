# defines the class of Customer and all functions that make up the customer object
class Customer:
    def __init__(self):
        self.name = None
        self.address = None
        self.phone = None
        self.balance = None

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setPhone(self, phone):
        # does not validate numerical entry but will check if entry length is 12
        if len(phone) == 12:
            self.phone = phone
            return True
        else:
            # coaxes user into formatting number entry
            print("Phone number must be formatted ###-###-####")
            return False

    def setBalance(self, balance):
        # validates numerical entry for balance as well as checking if entry is positive
        try:
            if int(balance) > 0:
                self.balance = balance
                return True
            else:
                print("Negative balance not allowed.")
                return False
        # catches non numerical entry and throws user into same path as if they entered negative number
        except ValueError:
            return False

    # function to print the customer info upon user request
    def printCustomer(self):
        print(self.name + " at " + self.address + " and phone number " + self.phone + " owes $ " + self.balance)
        return


# function to prompt user to request customer info
def pullCustomer():
    individual = raw_input("What customer would you like to list? ")
    for a in range(0, 5):
        if customers[a].name == individual:
            customers[a].printCustomer()


# defines the list of customers as customers
customers = list()
# appends entry to list of customers while looping user through validation tasks defined in the
# setPhone and setBalance functions above.
for i in range(0, 5):
    temp = Customer()
    temp.setName(raw_input("Input Name: "))
    temp.setAddress(raw_input("Input Address: "))
    while not temp.setPhone(raw_input("Input Phone: ")):
        print("Enter the phone again: ")
    while not temp.setBalance(raw_input("Input Balance: ")):
        print ('Entry must be a number! Please try again!')
    customers.append(temp)
# call to function to prompt for customer info request
pullCustomer()


retry = raw_input('Could not find customer.. Try again? y/n ')
if retry == 'y':
    pullCustomer()
elif retry == 'n':
    print('Exiting...')
else:
    print('Please enter y or n..')
