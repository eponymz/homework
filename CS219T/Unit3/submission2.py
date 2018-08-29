# class DVD
class DVD:

    # Constructor
    def __init__(self, title, dvd_Type, cost):
        self.title = title
        self.dvd_Type = dvd_Type
        self.cost = cost

    # newTitle
    def setTitle(self, newTitle):
        self.title = newTitle

    # Return self._title instance variable
    def getTitle(self):
        return self.title

    # Return self.type instance variable
    def getType(self):
        return self.dvd_Type

    # Return self.cost instance variable
    def getCost(self):
        return self.cost

    # Change the self._cost instance variable
    def setCost(self, newCost):
        self.cost = newCost

    # Change the self.dvd_type instance variable. This includes verifying the dvd_type specified will match validtypes
    def setType(self, newdvd_Type):
        validTypes = ['Game', 'Word', 'Compiler', 'Spreadsheet', 'dBase', 'Presentation']
        while True:
            dvd_Type = input('Please enter the valid type: (Game,Word,Compiler,Spreadsheet,dBase,Presentation)')
            if dvd_Type not in validTypes:
                print('Incorrect type, please enter from the following choices: '
                      '(Game,Word,Compiler,Spreadsheet,dBase,Presentation)')
                continue
            else:
                self.dvd_Type = newdvd_Type
            break

    # Take user entered information. Not used in this implementation.
    def loadInformation(self):
        __title = input('Enter a title of the DVD')
        __dvdtype = input('Enter the type of DVD')
        __cost = input('Please enter the cost')

    # define valid types that user can enter
    def listValidDVDTypes(self):
        print("We only accept: 'Game', 'Word', 'Compiler', 'Spreadsheet', 'Dbase', and 'Presentation' as the DVD Types")

    # output title,dvd_type, and cost
    def Display_DVD_Information(dvds):
        for obj in dvds:
            print(obj.title)
            print(obj.dvd_type)
            print(obj.cost)

    # Calculate average cost and output
    def DisplayTotalAndAverageCosts(dvds):
        add = 0
        for obj in dvds:
            add += obj.cost
        print(obj.cost)
        avg = add / len(dvds)
        print('Average cost: ', avg)

    # Allow user to change dvd title, type, and cost
    def ChangeDVD(A_DVD):
        # Show Current title and allow user to update
        print('DVD Title is', A_DVD.title)
        in1 = input('Do you want to change title(y/n):')
        if in1 in ['y', 'Y']:
            title = input('Please enter a title:')
            A_DVD.title = title
        else:
            pass

        # Show current type and allow user to update type
        print('DVD type is ', A_DVD.dvd_Type)
        in2 = input('Do you want to change type (y/n): ')
        if in2 in ['y', 'Y']:
            validTypes = ['Game', 'Word', 'Compiler', 'Spreadsheet', 'dBase', 'Presentation']
            while True:
                dvd_type = input('Please enter valid type: (Game,Word,Compiler,Spreadsheet,dBase,Presentation)')
                if dvd_type.title() not in validTypes:
                    print('Incorrect type, please enter from the following choices: '
                          '(Game,Word,Compiler,Spreadsheet,dBase,Presentation)')
                    continue
                else:
                    A_DVD.type = dvd_type
                break
            else:
                pass
        # Show current cost and allow user to update it
        print('DVD cost is ', A_DVD.cost)
        in3 = input('Do you want to change cost (y/n):')
        if in3 in ['y', 'Y']:
            cost = int(input('Please enter the cost: '))
            A_DVD.cost = cost
        else:
            pass


def main():
    # Create empty list
    dvdList1 = list()  # type: List[DVD]

    # Variables for adding to the list
    dvd1 = DVD('NBA 2K', 'Game', 45)
    dvd2 = DVD('MLB 2018', 'Game', 55)
    dvd3 = DVD('NFL 2K 2018', 'Game', 65)

    # Add data to list
    dvdList1.append(dvd1)
    dvdList1.append(dvd2)
    dvdList1.append(dvd3)
    print('All of the DVD information')

    # Display all dvd info
    DVD.Display_DVD_Information(dvdList1)

    # Display total cost and average of the cost
    DVD.DisplayTotalAndAverageCosts(dvdList)

    # Allow user to update list
    DVD.ChangeDVD(dvd1)
    DVD.ChangeDVD(dvd2)
    DVD.ChangeDVD(dvd3)

    # Declare new list
    dvdList = []

    # Add updated information to list
    dvdList.append(dvd1)
    dvdList.append(dvd2)
    dvdList.append(dvd3)

    # Display updated information list
    DVD.Display_DVD_Information(dvdList)

    # Display updated total cost and average
    DVD.DisplayTotalAndAverageCosts(dvdList)


main()
