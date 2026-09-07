from datetime import datetime

from mysql.connector import Error

from banking.db import (
    get_connection,
    find_user_by_nickname,
    get_balance_for_update,
    adjust_balance,
    insert_transaction,
)


def add_transaction():
    connect = get_connection()
    cursor = connect.cursor()
    try:
        sender_nickname = input("Enter sender nickname: ")
        sender = find_user_by_nickname(cursor, sender_nickname)
        if sender is None:
            print("Sender not found")
            return

        recipient_nickname = input("Enter recipient nickname: ")
        recipient = find_user_by_nickname(cursor, recipient_nickname)
        if recipient is None:
            print("Recipient not found")
            return

        if sender["id"] == recipient["id"]:
            print("Sender and recipient must be different users")
            return

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Amount must be a number")
            return

        if amount <= 0:
            print("Amount must be positive")
            return



        # FOR UPDATE locks this row until COMMIT/ROLLBACK, preventing
        # concurrent transactions from reading a stale balance
        sender_balance = get_balance_for_update(cursor, sender["id"])

        if sender_balance < amount:
            connect.rollback()
            print("Insufficient balance")
            return

        adjust_balance(cursor, sender["id"], -amount)
        adjust_balance(cursor, recipient["id"], amount)
        transaction_id = insert_transaction(cursor, sender["id"], recipient["id"], amount, datetime.now())

        connect.commit()
        print(f"Transaction complete: {amount} sent from {sender['user_nickname']} "
              f"to {recipient['user_nickname']} (id: {transaction_id})")

    except Error as e:
        connect.rollback()
        print("Transaction failed, rolled back:", e)
    finally:
        cursor.close()
        connect.close()


