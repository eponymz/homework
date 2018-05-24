def main():
    hourlytemps=[]

# this function collects input from the user and stores entries in a list.
    def GetTemperatures(hourlytemps):
        # defines the max length of the list i.e. 24, one for each hour
        while len(hourlytemps) < 25:
            # counter to print out hour next to temperature result
            for hours in range(-1, 24):
                hours += 1
                # collection happens here as well as appending ":00" purely for style reasons
                entry = raw_input("Enter the temperature for " + str(hours) + ":00. >> ")
                # validates that the entry is within the range of -50 - 130 // appends if true
                valid = bool(int(-50) < int(entry) < int(130))
                if valid:
                    hourlytemps.append(int(entry))
                # returns a prompt if validation fails
                else:
                    raw_input("Please enter a valid temperature between -50 and 130. >> ")
            break
    GetTemperatures(hourlytemps)

# function handles the math to compute average, highest, and lowest
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


