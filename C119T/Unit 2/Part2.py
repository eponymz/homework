from statistics import mean

# defines the variables used in the arithmetic operations below, and converts them to an "int" data type
num1 = input("Enter the first number. >> ")
num2 = input("Enter the second number. >> ")
num3 = input("Enter the third number. >> ")

# defining variables to make printing results easier
# the actual math happens here as well
numSum = num1 + num2 + num3
numAvg = mean([num1, num2, num3])
numProd = num1 * num2 * num3
numSmall = min(num1, num2, num3)
numBig = max(num1, num2, num3)

# prints results out with a new line between input request
print('\n')
print('Sum is ' + str(numSum))
print('Average is ' + str(numAvg))
print('Product is ' + str(numProd))
print('Smallest is ' + str(numSmall))
print('Largest is ' + str(numBig))

