# *** Update your existing User class to have an association with the BankAccount class.

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        return f"{self.balance}"
    
    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:

# 1. Update the User class __init__ method

# 5. SENSEI BONUS: Allow a user to have multiple accounts; 
# update methods so the user has to specify which account they are withdrawing or depositing to

    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(0.01, 6000),
            "saving" : BankAccount(0.03, 2000)
        }

# 2. Update the User class make_deposit method

    # def make_deposit(self, amount):
    #     self.amount += amount
    #     return self

# 3. Update the User class make_withdrawal method

    # def make_withdrawl(self, amount):
    #     self.amount -= amount
    #     return self

# 4. Update the User class display_user_balance method

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Saving Balance: {self.account['saving'].display_account_info()}")
        return self
    
    # def transfer_money(self, amount, user):
    #     self.amount -= amount
    #     user.amount += amount
    #     self.display_user_balance()
    #     user.display_user_balance()
    #     return self

hyunseok = User("Hyunseok")
hyunseok.account['checking'].deposit(3000).withdraw(2000)
hyunseok.account['saving'].deposit(2000).withdraw(400).yeild_interest()

hyunseok.display_user_balance()