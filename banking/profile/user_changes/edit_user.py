from banking.db import get_connection, find_user_by_id, update_user_field
from banking.validators import is_valid_email, is_valid_phone, is_strong_password, hash_password


def change_nickname(cursor, user_id):
    new_nickname = input("Enter new nickname: ")
    update_user_field(cursor, user_id, "nickname", new_nickname)
    print("Nickname changed")


def change_email(cursor, user_id):
    new_email = input("Enter new email: ")
    if not is_valid_email(new_email):
        print("Email not valid, nothing changed")
        return
    update_user_field(cursor, user_id, "email", new_email)
    print("Email changed")


def change_phone_number(cursor, user_id):
    new_phone = input("Enter new phone number: ")
    if not is_valid_phone(new_phone):
        print("Phone number not valid, nothing changed")
        return
    update_user_field(cursor, user_id, "phone_number", new_phone)
    print("Phone number changed")


def change_password(cursor, user_id):
    new_password = input("Enter new password: ")
    if not is_strong_password(new_password):
        print("Password too weak (min 8 chars + a symbol), nothing changed")
        return
    update_user_field(cursor, user_id, "password", hash_password(new_password))
    print("Password changed")


def update_user():
    connect = get_connection()
    cursor = connect.cursor()
    try:
        user_id = int(input("Enter user id: "))
        user = find_user_by_id(cursor, user_id)
        if user is None:
            print("User not found")
            return

        print("What do you want to change?")
        print("1. Nickname")
        print("2. Email")
        print("3. Phone number")
        print("4. Password")
        print("5. Cancel")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                change_nickname(cursor, user_id)
            case "2":
                change_email(cursor, user_id)
            case "3":
                change_phone_number(cursor, user_id)
            case "4":
                change_password(cursor, user_id)
            case "5":
                return
            case _:
                print("Invalid choice")
                return

        connect.commit()

    finally:
        cursor.close()
        connect.close()


if __name__ == "__main__":
    update_user()