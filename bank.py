from persons import User


class Bank:
    total_balance = 0
    loan_status = True
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.admin = []


    def find_user(self, ac_no):
        for user in User.user_list:
            if user.ac_no == int(ac_no):
                return user
        return None

    def set_admin(self, admin):
        self.admin.append(admin)
    # 1. Can create an account    
    def create_user(self, name, email, address, ac_type):
        new_user = User(name, email, address, ac_type)
        User.user_list.append(new_user)
        print(f"Successfully created account with {new_user.name}")
    
    # 2. Can delete any user account                                                             
    def delete_user(self, ac_no):
        for user in User.user_list:
            if user.ac_no == ac_no:
                User.user_list.remove(user)
                print(f'Successfully deleted {ac_no}')
                return
            print(f"No user was found with account no : {ac_no}")

    # 3. Can see all user accounts list
    def show_users(self):
        if User.user_list:
            print("Users: ")
            for user in User.user_list:
                print(f'Acc_no:{user.ac_no}, Name: {user.name}, Email: {user.email}, Address: {user.address},  Account Type: {user.ac_type}, Balance: {user.balance}')
        else:
            print("No users registered yet")
        

    # 4. Can check the total available balance of the bank.          
    def total_bank_balance(self):
        total_balance = 0
        for user in User.user_list:
            total_balance += user.balance
        print(f"Total bank balance = {total_balance}")

    # 5. Can check the total loan amount.                                                       
    def total_loan(self):
        total_loan = 0
        for user in User.user_list:
            total_loan += user.loan
        print(f"Total bank loan = {total_loan}")
        
    # 6. Can on or off the loan feature of the bank.                                       
    def loan_toggle(self, ac_no): 
        status = "On"
        user = self.find_user(ac_no)
        if user.loan_time == user.max_loan:
            status = "On"
            user.loan_time = 0
        else:
            status = "Off"
        print(f"Loan is {status} again for this user")
