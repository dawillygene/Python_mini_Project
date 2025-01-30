PSEUDOCODE:

START
    DEFINE class BankAccount
        INITIALIZE account holder name, balance, and account number
        DEFINE deposit(amount)
            ADD amount to balance
            DISPLAY new balance
        DEFINE withdraw(amount)
            IF amount is greater than balance
                DISPLAY "Insufficient funds"
            ELSE
                SUBTRACT amount from balance
                DISPLAY new balance
        DEFINE check_balance()
            DISPLAY current balance

    DEFINE function main()
        CREATE an empty dictionary to store bank accounts
        DISPLAY menu options
        LOOP:
            GET user choice
            IF choice is to create an account:
                ASK for name
                GENERATE a unique account number
                ADD new account to dictionary
            IF choice is deposit:
                ASK for account number and deposit amount
                CALL deposit function
            IF choice is withdraw:
                ASK for account number and withdraw amount
                CALL withdraw function
            IF choice is check balance:
                ASK for account number
                CALL check_balance function
            IF choice is exit:
                TERMINATE program

    CALL main()
END



Algorithm:

1.Define a BankAccount class with:
2.deposit()
3.withdraw()
4.check_balance()
5.Create a dictionary to store accounts.
6.Provide a menu for users:
7.Create Account
8.Deposit Money
9.Withdraw Money
10.Check Balance
11.Exit
12.Loop until the user exits.


Example 1: Creating an Account

Enter your name: Alice
Account created successfully! Your Account Number: 245678


Example 2: Depositing Money

Enter your account number: 245678
Enter amount to deposit: 500
Deposit successful! New balance: $500.00

Example 3: Withdrawing Money

Enter your account number: 245678
Enter amount to withdraw: 200
Withdrawal successful! New balance: $300.00

Example 4: Checking Balance
Enter your account number: 245678
Account Balance for Alice (A/C 245678): $300.00


Example 5: Trying to Withdraw More Than Available

Enter your account number: 245678
Enter amount to withdraw: 500
Insufficient funds!
