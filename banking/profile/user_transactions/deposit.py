from datetime import datetime

from mysql.connector import Error

from banking.db import get_connection, find_user_by_nickname, adjust_balance, insert_deposit


def deposit():
    connect = get_connection()
    cursor = connect.cursor()
    try:
        nickname = input("Enter your nickname: ")
        user = find_user_by_nickname(cursor, nickname)
        if user is None:
            print("User not found")
            return

        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Amount must be a number")
            return

        if amount <= 0:
            print("Amount must be positive")
            return


        adjust_balance(cursor, user["id"], amount)
        deposit_id = insert_deposit(cursor, user["id"], amount, datetime.now())
        connect.commit()

        print(f"Deposit complete: {amount} added to {user['user_nickname']}'s balance (id: {deposit_id})")

    except Error as e:
        connect.rollback()
        print("Deposit failed, rolled back:", e)
    finally:
        cursor.close()
        connect.close()


