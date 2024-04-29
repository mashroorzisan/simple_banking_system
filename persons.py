from abc import ABC
from transaction import Transaction

class Person(ABC):
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address
    

class User(Person):
    max_loan = 2
    user_list = []
    # 1. Can create an account with his/her name, email, address and account Type(Mainly Two Types: Savings & Current).
    # 2. Initially, the balance will be 0. An account number will be generated automatically. 									    5

    def __init__(self, name, email, address, ac_type) -> None:
        super().__init__(name, email, address)
        self.ac_type = ac_type
        self.balance = 0
        self.loan = 0
        self.ac_no = self.generate_ac_no() # auto generate ac no.
        self.transaction_history = []
        self.loan_time = 0
        # self.user_list.append(self)


    # auto generate account number

    def generate_ac_no(self):
        return len(self.user_list)+2008120
    
    # 3. Can deposit and withdraw amount. 
    # If the withdrawal amount is more than 
    # the current balance, show an error message that 
    # “Withdrawal amount exceeded”
    
    # make transaction
    def make_transaction(self, transaction_name, amount):
        transaction = Transaction(transaction_name, amount)
        self.transaction_history.append(transaction)
        print(transaction.time)
        print(f"{transaction_name} amount {amount} is successful!")
    
    def deposit(self,amount):
        if(amount>0):
            self.balance += amount
            self.make_transaction('Deposit', amount)

        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if(amount>0):
            if(amount<=self.balance):
                self.balance -= amount
                self.make_transaction('Withdraw', amount)
            else:
                print("Withdrawal amount exceeded")

        else:
            print("Invalid withdraw amount")

    # 4. Can check available balance. 
    def check_balance(self):
        print(f'Available balance of {self.name} is:- {self.balance} Taka only')
        

    # 5. Can check transaction history.  
    def check_transaction_history(self):
        print("Transaction History:- ")
        for tran in self.transaction_history:
            print(tran)


    # 6. Can take a loan from the bank at most two times.                                    4
    def issue_loan(self, amount):
        if self.loan_time < self.max_loan:
            if amount>0:
                self.balance += amount
                self.loan += amount
                self.loan_time += 1
                self.make_transaction('Loan', amount)
            else:
                print("Invalid amount")
        else:
            print('Sorry! You have already taken 2 loans. You can not take any more.')

  
      # 7. Can transfer the amount 
    # from his account to 
    # another user account. 
    # if the other account 
    # does not exist then 
    # show an error message 
    # “Account does not exist”.   

    def balance_transfer(self,sender_ac, reciver_ac, amount):
        if reciver_ac in self.user_list and sender_ac  in self.user_list:
            if amount > 0:
                if amount<=sender_ac.balance:
                    sender_ac.balance -= amount
                    sender_ac.make_transaction('Transfer', amount)
                    reciver_ac.balance += amount
                    reciver_ac.make_transaction('Recieve', amount)
                    print(f'Transferred {amount} BDT to {reciver_ac}')
                else:
                    print("Sorry! You don't have sufficient balance to transfer")
            else:
                print('Invalid amount')
        else:
            print(f"Accounts does not exist.")

    def __repr__(self) -> str:
        return f"{self.ac_no}"

class Admin(Person):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)