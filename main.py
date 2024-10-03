#Justine Tenorio
#Lab 11 program C
#This program is a menu driven verion of program A and B

#
#
#   This program uses the Account and CD classes from the accounts module to 
# create and manage the accounts. These classes likely have methods for depositing, 
# withdrawing, and retrieving account details.
#
#
import accounts

########################
DEPOSIT_SA = 1
WITHDRAW_SA = 2
DEPOSIT_CD = 3      #   <-Global Constants
WITHDRAW_CD = 4
BALANCE = 5
QUIT = 6
#########################

#
#
#   Asks the user to enter details about their savings accound and a CD
#   and creates an instance of savings and CD.
#   
#   Using the menu, the user can do plenty of options to do with their account.
#
#
def main():

    print('Enter the following data for a savings account.')
    acct_num = input('Account Number: ')
    int_rate = float(input('Inerest rate: '))
    balance = float(input('Balance: '))

    savings = accounts.Account(acct_num, int_rate, balance)

    #Get the account number, interest rate,
    #account balance, and maturity date for a CD
    print("Enter the following data for a CD.")
    acct_num = input('Account number: ')
    int_rate = float(input('Interest rate: '))
    balance = float(input('Balance: '))
    maturity = input('Maturity date: ')

    cd = accounts.CD(acct_num, int_rate, balance, maturity)
    
    choice = 0


    while choice != QUIT:
        choice = get_menu_choice()

        if choice == DEPOSIT_SA:
            deposit_sa(savings)
            
        elif choice == WITHDRAW_SA:
            withdraw_sa(savings)
            
        elif choice == DEPOSIT_CD:
            deposit_cd(cd)
            
        elif choice == WITHDRAW_CD:
            withdraw_cd(cd)
            
        elif choice == BALANCE:
            show_bal(savings, cd)
            
    exit = input("Press enter key to exit...")

#
#
#   prints all the choice you can make
#
#
def get_menu_choice():
    print()
    print('-----------------')
    print('Menu')
    print('-----------------')
    print("1. Make a deposit to your Savings")
    print("2. Make a withdrawal to your Savings")
    print("3. Make a deposit to your CD")
    print("4. Make a withdrawal to your CD")
    print("5. Show your current Balance")
    print("6. Quit the program")
    print()

    choice = int(input("Enter your choice: "))

    while choice < DEPOSIT_SA or choice > QUIT:
        choice = int(input("Enter a valid choice: "))

    return choice


#
#
#   Prompts the user for a withdrawal amount and subtracts it from the savings account.
#
#
def deposit_sa(savings):
    dep = float(input('How much would you like to deposit to your Savings? '))
    print('I will deposit that into your account.')
    savings.deposit(dep)
    print(savings)
    
    
#
#
#   Prompts the user for a withdrawal amount and subtracts it from the savings account.
#
#
def withdraw_sa(savings):
    cash = float(input('How much would you like to withdraw from your Savings? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)
    print(savings)


#
#
#   Prompts the user for a deposit amount and adds it to the CD.
#
#
def deposit_cd(cd):
    dep = float(input('How much would you like to deposit to your CD? '))
    print('I will deposit that into your account.')
    cd.deposit(dep)
    print(cd)
    

#
#
#   Prompts the user for a deposit amount and adds it to the CD.
#
#
def withdraw_cd(cd):
    cash = float(input('How much would you like to withdraw from your CD? '))
    print('I will withdraw that from your account.')
    cd.withdraw(cash)
    print(cd)

#
#
#   Displays the details and balances of both the savings account and the CD
#
#
def show_bal(savings, cd):
    print()
    print()
    print('Here is the data you entered: ')
    print()
    print('Savings Account')
    print('---------------')
    print('Account number: ', savings.get_account_num())
    print('Interest rate: ', savings.get_interest_rate())
    print(savings)
    print()
    print('CD')
    print('---------------')
    print('Account number: ', cd.get_account_num())
    print('Interest rate: ', cd.get_interest_rate())
    print(cd)
    print('Maturity date: ', cd.get_maturity_date())
    
main()
