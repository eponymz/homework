import math

# defines the value of the radius
radius = input("Enter the radius here. >> ")
# shortens the variable for easy typing but keeps the radius value isolated
r = radius

# prints the value of the area
print "The area of the circle is " + str(math.pi * r ** 2)
# prints the value of the circumference
print "The circumference of the circle is " + str(2 * math.pi * r)
# prints the value of the diameter
print "The diameter of the circle is " + str(r * 2)
