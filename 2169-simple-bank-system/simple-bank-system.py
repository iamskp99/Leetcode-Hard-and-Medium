class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def check(self,account):
        if account > len(self.balance) or account < 1:
            return False
        return True
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        ee = self.check(account1)&self.check(account2)
        if not ee:
            return ee

        a = account1-1
        b = account2-1
        if self.balance[a] < money:
            return False
        self.balance[a] -= money
        self.balance[b] += money
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        ee = self.check(account)
        if not ee:
            return ee
        account -= 1 
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        ee = self.check(account)
        if not ee:
            return ee

        account -= 1
        if self.balance[account] < money:
            return False
        self.balance[account] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)