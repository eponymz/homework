from transaction import Transaction


# BankStatement Class
class BankStatement:

    # Declaring constructor
    def __init__(self, initialBal=0.0):
        self.__BegBal = initialBal
        self.__EndBal = initialBal
        self.__TransactionLog = []
        self.__ArrangedLog = []
        self.__RunningBalLog = []
        self.__NumEntries = 0
        self.__NumDeposits = 0
        self.__NumWithdrawals = 0

    # Setter for beginning and end balance
    def setBegEndBals(self, BegEndBalance):
        self.__BegBal = self.__EndBal = BegEndBalance

    # Getter for beginning balance
    def getBegBal(self):
        return self.__BegBal

    # Getter for end balance
    def getEndBal(self):
        return self.__EndBal

    # Getter for number of entries
    def getNumEntries(self):
        return self.__NumEntries

    # Getter for number of deposits
    def getNumDeposits(self):
        return self.__NumDeposits

    # Getter for number of withdrawals
    def getNumWithDrawals(self):
        return self.__NumWithdrawals

    # Inset transaction method
    def insertTransaction(self, transaction):
        self.__TransactionLog.append(transaction)   # Appending this transaction to transaction log
        self.__NumEntries += 1  # Incrementing number of entries

        # If it is a withdrawal then add amount to last amount
        if transaction.getCode() == 'D':
            self.__NumDeposits += 1 # Incrementing number of deposits
            # if RunningBalLog is not empty get the last balance and add amount
            if len(self.__RunningBalLog) > 0:
                self.__EndBal = self.__RunningBalLog[-1] + transaction.getAmount()
                self.__RunningBalLog.append(self.__EndBal)  # Appending the end balance to running balance log
            else:
                # Otherwise, it means its the first transaction
                self.__EndBal = self.getBegBal() + transaction.getAmount()
                self.__RunningBalLog.append(self.__EndBal)
        elif transaction.getCode() == 'W':   # otherwise it is a withdrawal transaction i.e. deduct the amount
            self.__NumWithdrawals += 1
            if len(self.__RunningBalLog) > 0:
                self.__EndBal = self.__RunningBalLog[-1] - transaction.getAmount()
                self.__RunningBalLog.append(self.__EndBal)
            else:
                self.__EndBal = self.getBegBal() - transaction.getAmount()
                self.__RunningBalLog.append(self.__EndBal)

    # Displaying all transactions, beginning and end balances
    def displayResults(self):
        print("The beginning transaction was: $" + str(self.__BegBal))

        for index, t in enumerate(self.__TransactionLog):
            print("Transaction: " + str(index + 1) + " was a " +
                  t.getCode() + " amount: $" + str(t.getAmount()) + " for " + t.getNote())

            print("Running Bal: $" + str(self.__RunningBalLog[index]))

        print("The ending balance is: $" + str(self.__EndBal))
        print("The number of Transactions are: " + str(self.__NumEntries))
        print("The number of Deposits are: " + str(self.__NumDeposits))
        print("The number of Withdrawals are: " + str(self.__NumWithdrawals))

    # Arrange the current transactions
    def arrangeTransactions(self):
        del self.__ArrangedLog[:]  # Clearing current list

        # Loop through all the transactions and first add all Deposit transactions
        for t in self.__TransactionLog:
            if t.getCode() == 'D':
                self.__ArrangedLog.append(t)

        # Loop through all the transactions and finally add all Withdrawal transactions
        for t in self.__TransactionLog:
            if t.getCode() == 'W':
                self.__ArrangedLog.append(t)

    # Prints the arranged transactions
    def printArranged(self):
        print("Printing the Deposits and Withdrawals as a group:")
        for index, t in enumerate(self.__ArrangedLog):
            print("Transaction was a " + t.getCode() +
                  " amount: $" + str(t.getAmount()) + " for " + t.getNote())


# Start method to be called from main method
def start():
    myStatement = BankStatement()
    myStatement.setBegEndBals(15.92)

    # t = []
    # i = 0
    # while i < 5:
    #     t[i] = Transaction(getSetAmountVal, getSetCodeVal, getSetNoteVal)
    #     myStatement.insertTransaction(t[i])
    #     i += 1

    # t1 = Transaction(getSetAmountVal, getSetCodeVal, getSetNoteVal)
    t1 = Transaction()
    t1.loadTransaction()
    myStatement.insertTransaction(t1)

    t2 = Transaction()
    t2.loadTransaction()
    myStatement.insertTransaction(t2)

    t3 = Transaction()
    t3.loadTransaction()
    myStatement.insertTransaction(t3)

    t4 = Transaction()
    t4.loadTransaction()
    myStatement.insertTransaction(t4)

    t5 = Transaction()
    t5.loadTransaction()
    myStatement.insertTransaction(t5)

    # t3 = Transaction(getSetAmountVal, getSetCodeVal, getSetNoteVal)
    # myStatement.insertTransaction(t3)
    #
    # t4 = Transaction(getSetAmountVal, getSetCodeVal, getSetNoteVal)
    # myStatement.insertTransaction(t4)
    #
    # t5 = Transaction(getSetAmountVal, getSetCodeVal, getSetNoteVal)
    # myStatement.insertTransaction(t5)

    myStatement.displayResults()
    myStatement.arrangeTransactions()
    myStatement.printArranged()


# Main method of the program
if __name__ == '__main__':
    start()
