import transactions

from banking.db import list_transactions_for_user, get_connection, find_user_by_id

data = []

def find_user_info(user_id):
    for user in data:
        if user["id"] == user_id:
            return user
    return None

def find_user_transactions(user_id, resultant=None):
    result = []
    for transaction in transactions:
        if transaction.sender == user_id or transaction.recipient == user_id:
            result.append(transaction)
    return resultant

def view_transactions():
    connect = get_connection()
    cursor = connect.cursor()
    try:
        user_id = int(input("Enter user id: "))
        user = find_user_by_id(cursor, user_id)
        if user is None:
            print("User not found")
            return

        rows = list_transactions_for_user(cursor, user_id)
        if not rows:
            print("No transactions yet")
            return

        for row in rows:
            tx_id, sender_id, recipient_id, amount, created_at = row
            direction = "sent to" if sender_id == user_id else "received from"
            other_id = recipient_id if sender_id == user_id else sender_id
            print(f"[{created_at}] #{tx_id}: {amount} {direction} user {other_id}")

    finally:
        cursor.close()
        connect.close()

