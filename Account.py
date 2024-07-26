class Account:
    
    def __init__(self,bal,acc_no):
        self.balance=bal
        self.account_no=acc_no
    
    def setData(self):
        account_no=int(input("Enter account no:"))
        balance=int(input("Enter the balance in your account:"))
    
    def Debit(self):
        debit=int(input("Enter ammount to Debit :"))
        self.balance-=debit
        
    def Credit(self):
        credit=int(input("Enter ammount to credit :"))
        self.balance+=credit
        
    def print(self):
        print("Account no : ",self.account_no)
        print("Balance left in your account : ",self.balance)
        
acc1=Account(10000,8888)
acc1.Debit()
acc1.Credit()
acc1.print()