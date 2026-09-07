from banking.db import get_connection, find_user_by_id


def view_user():
    connect = get_connection()
    cursor = connect.cursor()
    try:
        user_id = int(input("Enter user id: "))
        user = find_user_by_id(cursor, user_id)

        if user is None:
            print("User not found")
            return

        print(f"ID: {user['id']}")
        print(f"Nickname: {user['user_nickname']}")
        print(f"First name: {user['first_name']}")
        print(f"Last name: {user['last_name']}")
        print(f"Email: {user['email']}")
        print(f"Phone number: {user['phone_number']}")
        print(f"Balance: {user['balance']}")

    finally:
        cursor.close()
        connect.close()


if __name__ == "__main__":
    view_user()