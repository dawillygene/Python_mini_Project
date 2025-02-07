import random

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.account_number = random.randint(100000, 999999) 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Account Balance for {self.name} (A/C {self.account_number}): ${self.balance:.2f}")


accounts = {}

def create_account():
    name = input("Enter your name: ")
    account = BankAccount(name)
    accounts[account.account_number] = account
    print(f"Account created successfully! Your Account Number: {account.account_number}")

def deposit_money():
    acc_num = int(input("Enter your account number: "))
    if acc_num in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_num].deposit(amount)
    else:
        print("Account not found!")

def withdraw_money():
    acc_num = int(input("Enter your account number: "))
    if acc_num in accounts:
        amount = float(input("Enter amount to withdraw: "))
        accounts[acc_num].withdraw(amount)
    else:
        print("Account not found!")

def check_balance():
    acc_num = int(input("Enter your account number: "))
    if acc_num in accounts:
        accounts[acc_num].check_balance()
    else:
        print("Account not found!")

def main():
    while True:
        print("\nWelcome to Simple Banking System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


main()
