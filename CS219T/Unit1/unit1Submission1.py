def main():
    # defines list of donors. This will contain a list of three items per donor
    donors = list()
    # the print was used in testing out formatting
    # print donors
    # this code assumes 5 donors were entered. Indefinite loop *could* be used here with appropriate break statements
    for x in xrange(4):
        x = 0
        # the following three lines accept input and store the value to a variable
        name = raw_input('Name: ')
        address = raw_input('Address: ')
        contact = raw_input('Contact: ')
        # appends the input variables respectively to their list inside donors[]
        donors.append(list([name, address, contact]))
        x += 1

    for i in range(len(donors)):
        for j in xrange(3):
            print (donors[i][j])


main()
