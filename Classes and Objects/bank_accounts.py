# Write code below 💖

class BankAccount:
    def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self):
        self.balance += int(input("Please Enter Deposit Amount: $"))
        print(f'Here is your new balance: ${self.balance}')
    def withdraw(self):
        self.balance -= int(input("Please Enter Withdrawl Amount: $"))
        print(f'Here is your new balance: ${self.balance}')
    def display_balance(self):
        print(f'Here is your current balance amount:  ${self.balance}')

Miley = BankAccount('Miley','Cyrus',1234,'Checkings',4567,1000)
Miley.deposit()
Miley.withdraw()
Miley.display_balance()

        
