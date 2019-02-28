# Class Account with name ,accNumber,balance
# Class Bank with bankName, branch,accountList(5 accounts)
# Implement following functions::
# A.accept_account_info
# B.print_account_info
# C.accept_bank_info
# D.print_bank_info
# E.delete_account
# #Return 1 if deleted else 0
# F.float deposit
# #Return updated balance
# G.float withdraw
# #Return updated balance


class Account:

    def __init__(self, accName , accNumber , accBalance):
        self._accName = accName
        self._accNumber = accNumber
        self._accBalance = accBalance

    def printAccount(self):
        print("Account Holder Name : {} , Account Number : {} , Account Balance {}".format(self._accName,self._accNumber, self._accBalance ))


    def calWithdrawal(self,aNumber , withdraw ):
        found = False
        if self._accNumber == aNumber:
            if int(withdraw) <  int(self._accBalance):
                left_balance = int(self._accBalance) - int(withdraw)
                self._accBalance = left_balance
            else:
                print("Sorry!!!! Account has insufficient Balance.transaction failed !!!!  Available Balance : {}".format(self._accBalance))
            found = True

        return found


    def calDeposit(self,aNumber , deposit ):
       found = False
       if self._accNumber == aNumber:
           added_balance = int(self._accBalance) + int(deposit)
           self._accBalance = added_balance

           found = True

       return found

    def delAccount(self,aNumber ):
       found = False
       if self._accNumber == aNumber:
           found = True

       return found




class Bank:

    def __init__(self, bankName= "** " , branch= "**" , accountList = []):
        self._bankName = bankName
        self._branch = branch
        baccountList = []
        for account in accountList:
            baccountList.append(Account(account._accName, account._accNumber, account._accBalance))
        self.__accountList =baccountList

    def printBank(self):
        print("Bank Name   :{} ".format(self._bankName))
        print("Bank Branch :{} ".format(self._branch))
        for ac in self.__accountList:
            ac.printAccount()

    def calculateDeposit(self, aNumber , deposit):
        for account in self.__accountList:
            found1 = account.calDeposit(aNumber, deposit)
            if found1 == True:
                print( " The details  of the account after deposit")
                account.printAccount()
                break;
        if found1 == False:
            print(" The account Number is not present !!!!")

    def calculateWithdraw(self, aNumber , withdraw):
        for account in self.__accountList:
            found2 = account.calWithdrawal(aNumber, withdraw)
            if found2 == True:
                print( " The details  of the account after withdrawal")
                account.printAccount()
                break;
        if found2 == False:
            print(" The account Number is not present !!!!")

    def deleteAccount(self, aNumber):
        for account in self.__accountList:
            found2 = account.delAccount(aNumber)
            if found2 == True:
                self.__accountList.remove(account)
                print( " Warning !!! Account is deleted ")
                break;
        if found2 == False:
            print(" The account Number is not present !!!!")





def main_function():
    print("Enter the account details for 5 account  ")
    input_accList = []
    for i in range(0,2):
        input_accName   = input("Account Holder Name : ")
        input_accNumber = input("Account Number      : ")
        input_accBalance= input("Account Balance     : ")
        A1 = Account(input_accName, input_accNumber, input_accBalance)
        input_accList.append(A1)

    print("Enter the bank information   : ")
    input_bankName= input("Bank Name    : ")
    input_branch  = input("Branch Name  : ")

    print(" ")
    print("           ***  The details of the accounts are  *** ")
    for account in input_accList:
        account.printAccount()

    print(" ")
    print("           ***  The details of the Bank are  *** ")

    B1 = Bank(input_bankName, input_branch, input_accList)
    B1.printBank()

    print("..........................................................................")
    input_option = input("Enter the option 1. Deposit     2. Withdrawsal :")
    if input_option == '1':
        print(" Enter the account Number and amount to be deposited :")
        input_aNumber = input("Account Number : ")
        input_deposit  = input("Deposit Amount  : ")
        B1.calculateDeposit(input_aNumber, input_deposit)
    elif input_option =='2':
        print(" Enter the account Number and amount to be withdraw :")
        input_aNumber = input("Account Number : ")
        input_withdraw  = input("Withdraw Amount  : ")
        B1.calculateWithdraw(input_aNumber, input_withdraw)
    else:
        print("You have entered the wrong option !!!!")

    print("............................................................................")
    input_Delete = input("Do you want to delete the account  y / n ? : ")
    if input_Delete == 'y':
        input_delAccNumber = input("Enter the account number to be deeted : ")
        B1.deleteAccount(input_delAccNumber)
        print()
        print("The Updated Bank and Account details are : ")
        B1.printBank()




main_function()










