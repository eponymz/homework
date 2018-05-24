def main():
    hourlytemps=[]

    # this function collects input from the user and stores entries in a list.
    def GetTemperatures(hourlytemps):
        # defines the max length of the list i.e. 24, one for each hour
        while True:
            # counter to print out hour next to temperature result
            for hours in range(-1, 24):
                hours += 1
                # collection happens here as well as appending ":00" purely for style reasons
                if hours < 10:
                    entry = raw_input("Enter the temperature for " + "0" + str(hours) + ":00. >> ")
                    try:
                        # validates that the entry is within the range of -50 - 130 // appends if true
                        # defines entry as int()
                        valid = bool(int(-50) < int(entry) < int(130))
                        if valid:
                            hourlytemps.append(int(entry))

                        else:
                            # returns a prompt if validation fails
                            entry = raw_input("Please enter a valid temperature between -50 and 130 for " + str(hours) + ". >> ")
                            try:
                                valid = bool(int(-50) < int(entry) < int(130))
                                if valid:
                                    hourlytemps.append(int(entry))

                            except ValueError:
                                print "You must enter a number in the valid range. Please restart program."
                                return
                            # continues while loop
                            continue
                    except ValueError:
                        # catches value error if alpha characters are entered
                        entry = raw_input("Please enter a valid temperature between -50 and 130 for " + str(hours) + ". >> ")
                        try:
                            valid = bool(int(-50) < int(entry) < int(130))
                            if valid:
                                hourlytemps.append(int(entry))

                        except ValueError:
                            print "You must enter a number in the valid range. Please restart program."
                            return
                # this portion of the while loop is exactly the same as the if statement. Difference is it does not prepend a 0
                else:
                    entry = raw_input("Enter the temperature for " + str(hours) + ":00. >> ")
                    try:
                        valid = bool(int(-50) < int(entry) < int(130))
                        if valid:
                            hourlytemps.append(int(entry))

                        else:
                            entry = raw_input("Please enter a valid temperature between -50 and 130 for " + str(hours) + ". >> ")
                            try:
                                valid = bool(int(-50) < int(entry) < int(130))
                                if valid:
                                    hourlytemps.append(int(entry))

                            except ValueError:
                                print "You must enter a number in the valid range. Please restart program."
                                return
                            continue
                    except ValueError:
                        entry = raw_input("Please enter a valid temperature between -50 and 130 for " + str(hours) + ". >> ")
                        try:
                            valid = bool(int(-50) < int(entry) < int(130))
                            if valid:
                                hourlytemps.append(int(entry))

                        except ValueError:
                            print "You must enter a number in the valid range. Please restart program."
                            return

            break
        # the following statement was in place for troubleshooting an IndexError I had run into
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


