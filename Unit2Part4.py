numEntry = input("Enter a number to determine if it is odd or even >")

# takes the input number and calculates the remainder when divided by 2
# if remainder is 0 then the number is divisible by 2 and therefore even
if numEntry % 2 == 0:
    print("The number is even!")
# if the remainder is not 0 (only other option being 1) then the number is not divisible by 2 and is therefore odd
else:
    print("The number is odd!")


# another way of writing this program would be to use the while function
while numEntry % 2 == 0:
    print("The number is even!!")
    break
else:
    print("The number is odd!!")
