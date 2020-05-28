import sys

#


class mainStorage():
    accHolderNames = ["Carlos", "Rick", "Morty"]
    pinNumbers = [2835, 1293, 5041]
    balance = [500, 500, 500]
    enteringAMT = [500, 500, 500]

    def display(self):
        i = 0
        while i < len(self.accHolderNames):
            print("\n")
            print("Name : ", self. accHolderNames[i])
            print("Pin Number : ", self.pinNumbers[i])
            print("Current Balance : ", self.balance[i])
            print("Entering Balance : ", self.enteringAMT[i])
            i += 1
        MainMenu()

# -----------------------------------------------------------------------------
# accessAcc class
# This class involves accessing the parent classes list which acts as a data storage


class accessAcc(mainStorage):  # Applying Single inheritence
    # Temporary storages which will later be converted into a dictionary
    tempName = ""
    tempPin = 0
    tempEntAmt = 0
    tempBal = 0
    tempDeduct = 0
    tempDeposit = 0
    pinStatus = False
    # Function that is used to create a new account

    def newAccount(self):
        self.tempName = input("Enter Name of New Account Holder : ")
        self.tempPin = int(input("Enter a suitable four number pin : "))
        while self.tempEntAmt < 499:  # Not allowing inputs less than 500
            self.tempEntAmt = int(input("Enter an entering amount : "))
            if(self.tempEntAmt < 499):
                print("Insufficient amount less than 500 is invalid")
        # Storing temporary values into the data storage
        self.accHolderNames.append(self.tempName)
        self.pinNumbers.append(self.tempPin)
        self.balance.append(self.tempEntAmt)
        self.enteringAMT.append(self.tempEntAmt)
        # Outputting the values inputted
        i = 0
        while i < len(self.accHolderNames):
            print("\n")
            print("Name : ", self. accHolderNames[i])
            print("Pin Number : ", self.pinNumbers[i])
            print("Current Balance : ", self.balance[i])
            print("Entering Balance : ", self.enteringAMT[i])
            i += 1
        MainMenu()
    # Function that allows the user to edit the details of the account

    def editAccount(self):
        print("Enter the following numbers to edit the following details")
        print("1 - Name")
        print("2 - Pin Num")
        choice = int(input("Enter here : "))
        i = 0
        update = False
        if choice == 1:
            self.tempName = input("Enter name : ")
            while i < len(self.accHolderNames):
                if self.tempName == self.accHolderNames[i]:
                    self.tempName = input("Update name : ")
                    self.accHolderNames[i] = self.tempName
                    update = True
                    break
                else:
                    update = False
                    continue
            if update == True:
                print("Details updated! ")
        MainMenu()

    def deposit(self):
        i = 0
        while self.pinStatus != True:
            self.tempPin = int(input("Enter Pin again"))
            while i < self.pinNumbers[i]:
                if self.tempPin == self.pinNumbers[i]:
                    print("Welcome ", self.accHolderNames[i])
                    self.tempDeposit = int(
                        input("Enter amount for deposit : "))
                    self.balance[i] += self.balance[i] + self.tempDeposit
                    print("Deposit Complete! Returning to main menu")
                    self.pinStatus = True
                    break
                if self.tempPin != self.pinNumbers[i]:
                    self.pinStatus = False
                    continue
            if self.pinStatus == False:
                print("Your Pin is incorrect ,returning to main menu")
                break
        MainMenu()

    def withdraw(self):
        i = 0
        while self.pinStatus != True:
            self.tempPin = int(input("Enter Pin again"))
            while i < self.pinNumbers[i]:
                if self.tempPin == self.pinNumbers[i]:
                    print("Welcome ", self.accHolderNames[i])
                    self.tempDeduct = int(
                        input("Enter amount for withdraw : "))
                    self.balance[i] += self.balance[i] - self.tempDeduct
                    print("Deposit Complete! Returning to main menu")
                    self.pinStatus = True
                    break
                if self.tempPin != self.pinNumbers[i]:
                    self.pinStatus = False
                    continue
            if self.pinStatus == False:
                print("Your Pin is incorrect ,returning to main menu")
                break
        MainMenu()

        def balance(self):
            i = 0
            while self.pinStatus != True:
                self.tempPin = int(input("Enter Pin again"))
                while i < self.pinNumbers[i]:
                    if self.tempPin == self.pinNumbers[i]:
                        print("Welcome ", self.accHolderNames[i])
                        print("Balance :", self.balance[i])
                        self.pinStatus = True
                        break
                    if self.tempPin != self.pinNumbers[i]:
                        self.pinStatus = False
                        continue
                if self.pinStatus == False:
                    print("Your Pin is incorrect ,returning to main menu")
                    break
        MainMenu()
# ---------------------------------------------------------------------------

        # Function used to display the main menu


def MainMenu():
    print(" \n \n ")
    print(" \t \t Welcome To Carlos Banking Management System \n ")
    print(" \t \t To enter a new account please enter : 1 \n ")
    print(" \t \t To update an account please enter : 2 \n ")
    print(" \t \t To Withdraw from account enter : 3 \n ")
    print(" \t \t To Deposit from an account enter : 4 \n ")
    print(" \t \t To view balance of an account  1enter : 5 \n ")
    print(" \t \t To view an accounts details enter : 6 \n ")
    print(" \t \t To close the program enter :  7 ")
    print("\n \n ")
    menuChoice = 0
    while menuChoice != 7:
        menuChoice = int(input(" Enter Here : "))
        accessStorage = mainStorage()
        accountDetails = accessAcc()
        if menuChoice == 1:
            accountDetails.newAccount()
            break
        elif menuChoice == 2:
            accountDetails.editAccount()
            break
        elif menuChoice == 3:
            accountDetails.withdraw()
            break
        elif menuChoice == 4:
            accountDetails.deposit()
            break
        elif menuChoice == 5:
            accountDetails.balance()
            break
        elif menuChoice == 6:
            accountDetails.display()
            break
        elif menuChoice == 7:
            sys.exit(0)
        else:
            # outputting an error for an invalid input
            raise Exception(" ERROR INVALID INPUT ")


MainMenu()
# Calling the Main Menu function
