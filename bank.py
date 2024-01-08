import sys


class Customer:
    bank_name = 'SBI'

    def __init__(self, name, passbook_number, balance):
        self.name = name
        self.passbook_number = passbook_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Hi {self.name}, your account Balance is: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Hi {self.name}, your account  have doesn\'t have sufficient Balance to withdraw amount')
            sys.exit(0)
        else:
            self.balance = self.balance - amount
            print(
                f'Hi {self.name}, your account balance after withdrawing the amount {amount} and the balance is :{self.balance}')

    def check_balance(self):
        print(f'Hi {self.name}, your account balance is :{self.balance}')


print('Welcome to SBI, Kindly enter your Account no')
passbook_number = input('Enter the Account No: ')
if len(passbook_number) == 11:
    name = input('Enter the name of the customer:\t')
    print(f'Hi, {name}, welcome to {Customer.bank_name} application')
    r1 = Customer(name=name, passbook_number = passbook_number, balance=0.0)
    print()
    while True:
        print('Select Your Option : \n d/D - Deposit \n w/W - Withdraw \n c|C - Check Balance \n e/E - Exit')
        print()
        option = input(f' Hi {name},Enter your option: ')
        print()
        if option == 'd' or option == 'D':
            amount = int(input(f' Hi {name}, Enter the amount to deposit in your account:\t'))
            r1.deposit(amount)

        elif option == 'w' or option == 'W':
            amount = int(input(f' Hi {name}, Enter the amount to withdraw from your account:\t'))
            r1.withdraw(amount)

        elif option == 'c' or option == 'C':
            r1.check_balance()

        elif option == 'e' or option == 'E':
            print(f'Thank you for using {Customer.bank_name} App')
            sys.exit(0)

        else:
            print('option invalid')
else:
    print('Account number is not matching, kindly check the Account number')
