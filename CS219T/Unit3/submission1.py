class MySum(object):
    def __init__(self, other1, other2, other3):
        self.other1 = other1
        self.other2 = other2
        self.other3 = other3

    def __str__(self):
        return '%s plus %s plus %s' % (self.other1, self.other2, self.other3)

    def __add__(self):
        if isinstance(self, set):
            pass
        elif self == '5':
            return '%s plus %s plus %s' % (self, other1, other2)
        return str(self) + other1 + other2 + other3

    def __radd__(self, other):
        return other + str(self)


result = MySum("5", "7", "9")
print("\nExample of overloading the _add_ method (fixed a bug here in the example code professor): " + result)


firstNum = 5
secondNum = 7
thirdNum = 9
total = firstNum + secondNum + thirdNum
print('The sum of {0} and {1} and {2} is {3}'.format(firstNum, secondNum, thirdNum, total))

firstList = [1, 2, 3, 4, 5]
secondList = [6, 7, 8, 9, 10]
thirdList = [11, 12]
concatenatedNewList = firstList + secondList + thirdList
print('Lets concatenate {2}, {0}, and {1} into a new list.\n'.format(firstList, secondList, thirdList))
print('The concatenated new list is {} \n'.format(concatenatedNewList))

stringOne = "Overloading / Overriding Example of "
stringTwo = "Python String "
stringThree = "for our class"
concatenatedNewString = stringOne + stringTwo + stringThree
print('The concatenated new string is {} '.format(concatenatedNewString))