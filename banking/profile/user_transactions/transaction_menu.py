from banking.profile.user_transactions.add_transaction import add_transaction
from banking.profile.user_transactions.transactions import view_transactions


def transaction_menu():
    print("---------Transactions---------")
    print("1. Send transaction")
    print("2. View transaction history")
    print("3. Back")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            add_transaction()
        case "2":
            view_transactions()
        case "3":
            return
        case _:
            print("Invalid choice")


