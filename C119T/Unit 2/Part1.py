# order of math operations


x = 7 + 3 * 6 / 2 - 1
#     ^3  ^1  ^2  ^4
print "x = " + str(x)

#####
# the modulus operator is executed after multiply/divide
x = 2 % 2 + 2 * 2 - 2 / 2
#     ^3  ^4  ^1  ^5  ^2
print "x = " + str(x)

#####
# parenthesis have the highest precedence i.e. they are the most binding
x = (3 * 9 * (3 + (9 * 3 / 3)))
#      ^5  ^4   ^3   ^1  ^2
print "x = " + str(x)
