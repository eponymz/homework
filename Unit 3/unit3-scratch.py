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
                                continue
                        except ValueError:
                            print "You must enter a number in the valid range. Please restart program."
                            return

            break
        print len(hourlytemps)
    GetTemperatures(hourlytemps)


main()

