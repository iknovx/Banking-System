from banking.db import get_connection, find_user_by_id, delete_user_by_id
from mysql.connector import Error


def delete_user():
    connect = get_connection()
    cursor = connect.cursor()
    try:
        user_id = int(input("Enter user id: "))
        user = find_user_by_id(cursor, user_id)
        if user is None:
            print("User not found")
            return

        confirm = input(f"Delete user '{user['user_nickname']}'? (yes/no): ")
        if confirm.lower() != "yes":
            print("Cancelled")
            return

        try:
            delete_user_by_id(cursor, user_id)
            connect.commit()
            print("User deleted")
        except Error:
            connect.rollback()
            print("Cannot delete: this user has transaction or deposit history")

    finally:
        cursor.close()
        connect.close()


