#Justine Tenorio
#Lab 11 account.py script

class Account:
    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_interest_rate(self,int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal
        
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

    def get_account_num(self):
        return self.__account_num

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return 'Balance: ' + format(self.__balance, ',.2f')

class CD(Account):

    #The init method accpets argumentsfor the\
    #account number, interest rate, balance and
    #maturity date

    def __init__(self, account_num, int_rate, bal, mat_date):
        #Call the superclass __init__ method
        Account.__init__(self, account_num, int_rate, bal)

        #Initialize the maturity_date attribute.
        self.__maturity_date = mat_date

    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    #The get_maturity_date method is an accessor
    #for the __maturity_date attribute

    def get_maturity_date(self):
        return self.__maturity_date
