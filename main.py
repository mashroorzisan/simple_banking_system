from bank import Bank
from persons import User, Admin
bank = Bank("ABC Bank", "dhaka")
admin = Admin("Admin", "admin@abc.com", "Admin's Address")
bank.set_admin(admin)

while True:
    print("****Bank****")
    print("Enter a for User")
    print("Enter b for Admin")
    print("Enter c to exit")
    choice = input("Login as User/Admin?: ")

    if choice == 'a':
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Take Loan")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Transaction History")
        print("7. Exit")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            ac_no = input("Enter your account number: ")
            amount = float(input("Enter the amount to deposit: "))
            user = bank.find_user(ac_no)
            if user:
                user.deposit(amount)
            else:
                print("User not found.")
        elif user_choice == '2':
            ac_no = input("Enter your account number: ")
            amount = float(input("Enter the amount to withdraw: "))
            user = bank.find_user(ac_no)
            if user:
                user.withdraw(amount)
            else:
                print("User not found.")
        elif user_choice == '3':
            ac_no = input("Enter your account number: ")
            amount = float(input("Enter the loan amount: "))
            user = bank.find_user(ac_no)
            if user:
                user.issue_loan(amount)
            else:
                print("User not found.")
        elif user_choice == '4':
            ac_no = input("Enter sender account no: ")
            re_ac_no = input("Enter receiver account no: ")
            sender = bank.find_user(ac_no)
            receiver = bank.find_user(re_ac_no)
            if receiver:
                amount = float(input("Enter the amount to transfer: "))
                sender.balance_transfer(sender, receiver, amount)
            else:
                print("No receiver found with this account")
        elif user_choice == '5':
            ac_no = input("Enter your account number: ")
            user = bank.find_user(ac_no)
            if user:
                user.check_balance()
            else:
                print("User not found.")
        elif user_choice == '6':
            ac_no = input("Enter your account number: ")
            user = bank.find_user(ac_no)
            if user:
                user.check_transaction_history()
            else:
                print("User not found.")
        elif user_choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    elif choice == 'b':
        print(f"\nWelcome to {bank.name} Management System")
        print("1. Create User Account")
        print("2. Delete User Account")
        print("3. Show All User Account")
        print("4. Check Total Bank Balance")
        print("5. Check Total Loan Amount")
        print("6. Loan (on/off)")
        print("7. Exit")
        admin_choice = input("Enter your choice: ")

        if admin_choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            address = input("Enter user address: ")
            ac_type = input("Entebr user account type (Savings/Current): ")
            bank.create_user(name, email, address, ac_type)

        elif admin_choice == '2':
            ac_no = int(input('Enter account no : '))
            bank.delete_user(ac_no)

        elif admin_choice == '3':
            bank.show_users()

        elif admin_choice == '4':
            bank.total_bank_balance()

        elif admin_choice == '5':
            bank.total_loan()

        elif admin_choice == '6':
            ac_no = int(input('Enter account no : '))
            bank.loan_toggle(ac_no)

        elif admin_choice == '7':
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice.")

    elif choice == 'c':
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid option. Please try again.")
