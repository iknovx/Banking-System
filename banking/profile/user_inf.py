from banking.profile.user_changes.add_user import add_user
from banking.profile.user_changes.edit_user import update_user
from banking.profile.user_changes.delete_user import delete_user
from banking.profile.user_changes.view_users import view_user


def user_info():
    print("---------Welcome to Bank---------")
    print("What do you want to do?")
    print("1. Add user")
    print("2. Update user")
    print("3. Delete user")
    print("4. View user")
    print("5. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            add_user()
        case "2":
            update_user()
        case "3":
            delete_user()
        case "4":
            view_user()
        case "5":
            print("Thank you for your time")
            return
        case _:
            print("Invalid choice")


