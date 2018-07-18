import itertools


def main():
    # declare any necessary variable(s)
    userList = []
    while True:
        for index in itertools.count():
            index += 1
            listEntry = raw_input("Enter a minimum of 8 words for your list. (type 'C' to complete your list).. >> ")

            userList.append(str(listEntry))

        print(userList)
        return


    # // Loop: while the user wants to continue processing more lists of words
    #
    #     // Loop: while the user want to enter more words (minimum of 8)
    #         // Prompt for, input and store a word (string) into a list
    #         // Pass the list of words to following functions, and perform the manipulations
    #
    #         //  to produce and return a new, modified, copy of the list.
    #           NOTE: None of the following functions can change the list parameter it
    #           receives the manipulated items must be returned as a new list.
    #
    #   // SortByIncreasingLength()
    #   // SortByDecreasingLength()
    #   // SortByTheMostVowels()
    #   // SortByTheLeastVowels()
    #   // CapitalizeEveryOtherCharacter()
    #   // ReverseWordOrdering()
    #   // FoldWordsOnMiddleOfList()
    #     // Display the contents of the modified lists of words
    #
    # // Ask if the user wants to process another list of words

main()
