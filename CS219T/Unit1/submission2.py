# creates the list for cars "empty garage"
garage = list()

# code assumes only 5 cars are entered
for x in xrange(5):
    newCar = raw_input('Enter car to add: ')
    garage.append(newCar)

# variable to watch when looping list
pickupCar = raw_input('Which car do you want to retrieve? >')

# counter plus 'search' loop
tick = 0
while garage.pop() != pickupCar:
    tick += 1

# sets estimated time to retrieve at 5 minutes
estTime = (tick+1) * 5

print("Estimated retrieval time is %s minutes." % estTime)
