import hashlib
import re

EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PASSWORD_SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*']


def is_valid_email(email: str) -> bool:
    return bool(re.match(EMAIL_PATTERN, email))


def is_valid_phone(phone: str) -> bool:
    return phone.isdigit() and 7 <= len(phone) <= 15


def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    return any(symbol in password for symbol in PASSWORD_SYMBOLS)


def is_positive_amount(value: str) -> bool:
    try:
        return float(value) > 0
    except ValueError:
        return False


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()