#Name: Vedant Dawange


#OOP's class and objects

# Creating class
class BankAcc:
    # init function to declare variables
    def __init__(self):
        self.balance = 0

    # Function to Deposit
    def deposit(self):
        amt = float(input("Enter Amount to Deposit"))
        self.balance += amt
        print("Current amount present is Rs.", self.balance)

    # Function To withdraw
    def withdraw(self):
        wit = float(input("Enter amount to be withdrawn"))
        if self.balance >= wit:
            self.balance -= wit
            print("You withdrew Rs.", wit)
        else:
            print("Insufficient balance")

    # Function to display the balance
    def display(self):
        print("Balance remaining is Rs.", self.balance)


# creating customer object
customer = BankAcc()

# calling functions of class BankAcc using object 'customer'

customer.deposit()
customer.withdraw()
customer.display()
