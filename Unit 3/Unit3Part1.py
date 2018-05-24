def main():
    hourlytemps=[]


    def GetTemperatures(hourlytemps):
        while True:
            for hours in range(-1, 24):
                hours += 1
                if hours < 10:
                    entry = raw_input("Enter the temperature for " + "0" + str(hours) + ":00. >> ")
                    try:
                        valid = bool(int(-50) < int(entry) < int(130))
                        if valid:
                            hourlytemps.append(int(entry))
                        else:
                            raw_input("Please enter a valid temperature between -50 and 130 for " + str(hours) + ". >> ")
                            continue
                    except ValueError:
                        entry = raw_input("Please enter a valid temperature between -50 and 130 for " + str(hours) + ". >> ")
                        try:
                            valid = bool(int(-50) < int(entry) < int(130))
                            if valid:
                                hourlytemps.append(int(entry))
                                continue
                        except ValueError:
                            print "You must enter a number in the valid range. Please restart program."
                            return

                else:
                    entry = raw_input("Enter the temperature for " + str(hours) + ":00. >> ")
                    try:
                        valid = bool(int(-50) < int(entry) < int(130))
                        if valid:
                            hourlytemps.append(int(entry))
                        else:
                            raw_input("Please enter a valid temperature between -50 and 130 for " + str(hours) + ". >> ")
                            continue
                    except ValueError:
                        entry = raw_input("Please enter a valid temperature between -50 and 130 for " + str(hours) + ". >> ")
                        try:
                            valid = bool(int(-50) < int(entry) < int(130))
                            if valid:
                                hourlytemps.append(int(entry))
                                continue
                        except ValueError:
                            print "You must enter a number in the valid range. Please restart program."
                            return

            break
        print "There are " + str(len(hourlytemps)) + " total entries."
    GetTemperatures(hourlytemps)

# this function handles the math to compute average, highest, and lowest
    def averagetemp(hourlytemps):
        highest = max(hourlytemps)
        lowest = min(hourlytemps)
        total = sum(hourlytemps)
        count = len(hourlytemps)
        average = total/count
        print "\n\nHighest temp is: ", str(highest)
        print "Lowest temp is: ", str(lowest)
        print "Average temp is: ", int(average)

# function to display all results + computed results
    def display(hourlytemps, averagetemp):
        # another counter to iterate the display to appear as a table
        # adds a line feed as well as appending ":00" and tab spaces
        for hour in range(-1, 24):
            hour += 1
            # prepends a zero to maintain style if the hour is less than 10
            if hour < 10:
                print "\n" + "0" + str(hour) + ":00\t\t".expandtabs() + str(hourlytemps[hour])
            else:
                print "\n" + str(hour) + ":00\t\t".expandtabs() + str(hourlytemps[hour])
        # executes computation function
        averagetemp(hourlytemps)
# executes display function
    display(hourlytemps, averagetemp)
main()


