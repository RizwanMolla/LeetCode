class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Validate account numbers
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False
        # Validate sufficient balance in sender account
        if self.balance[account1 - 1] < money:
            return False
        
        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # Validate account number
        if not (1 <= account <= self.n):
            return False
        
        # Deposit money
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Validate account number
        if not (1 <= account <= self.n):
            return False
        # Validate sufficient balance
        if self.balance[account - 1] < money:
            return False
        
        # Withdraw money
        self.balance[account - 1] -= money
        return True
