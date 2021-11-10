class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self
    
    def make_withdrawl(self, amount):
        self.amount -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self
    
    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self
