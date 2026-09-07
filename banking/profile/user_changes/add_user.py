from banking.db import (
    get_connection,
    find_user_by_nickname,
    find_user_by_email,
    find_user_by_phone,
    insert_user,
)
from banking.validators import (
    is_valid_email,
    is_valid_phone,
    is_strong_password,
    is_positive_amount,
    hash_password,
)

PROMPTS = {
    "nickname": "Enter your nickname: ",
    "first_name": "Enter your first name: ",
    "last_name": "Enter your last name: ",
    "email": "Enter your email: ",
    "phone_number": "Enter your phone number: ",
    "balance": "Enter your starting balance: ",
}


def validate_fields(cursor, values):
    errors = []

    if find_user_by_nickname(cursor, values["nickname"]):
        print("Nickname is already taken")
        errors.append("nickname")

    if not is_valid_email(values["email"]):
        print("Email is invalid")
        errors.append("email")
    elif find_user_by_email(cursor, values["email"]):
        print("Email is already taken")
        errors.append("email")

    if not is_valid_phone(values["phone_number"]):
        print("Phone number is invalid")
        errors.append("phone_number")
    elif find_user_by_phone(cursor, values["phone_number"]):
        print("Phone number is already taken")
        errors.append("phone_number")

    if not is_positive_amount(values["balance"]):
        print("Balance must be a number greater than 0")
        errors.append("balance")

    return errors


def add_user():
    connect = get_connection()
    cursor = connect.cursor()
    try:
        values = {field: input(prompt) for field, prompt in PROMPTS.items()}
        password = input("Enter your password: ")
        while not is_strong_password(password):
            print("Password must be at least 8 characters and include a symbol (!@#$%^&*)")
            password = input("Enter your password: ")

        while True:
            errors = validate_fields(cursor, values)
            if not errors:
                break
            print("Try again")
            for field in errors:
                values[field] = input(PROMPTS[field])

        new_id = insert_user(
            cursor,
            nickname=values["nickname"],
            first_name=values["first_name"],
            last_name=values["last_name"],
            email=values["email"],
            phone_number=values["phone_number"],
            password_hash=hash_password(password),
            balance=float(values["balance"]),
        )
        connect.commit()
        print(f"User added, id: {new_id}")

    finally:
        cursor.close()
        connect.close()

