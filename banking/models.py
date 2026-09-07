class User:
    def __init__(self,nickname,balance,id,first_name,last_name,email,phone_number,password):
        self.id = id
        self.user_nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.balance = balance


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount


class Deposit:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount