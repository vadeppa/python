'''
create a banking application,to check current balance,to deposite,to withdraw.

account class
atributes-name,balance,min_balance
methods-deposite,withdraw,printstatement

currentaccount class.....currentaccount balance
atributes-name,balance
methods- __str__
give min_balance


saving account class.....currentaccount balance
atributes-name,balance
methods- __str__

deposit rs.5000 in saving account
withdraw rs.7000 from saving

input:
1.print current balance
2.print current balance after deposit-5000
3.print current balance after withdraw-10000
4.withdraw 6000 rupees

output:
1.print current balance 10000
2.print current balance after deposit-15000
3.print current balance after withdraw-5000
4.insufficient balance
'''
class Account:
    def __init__(self,name,balance,minbalance):
        self.name=name
        self.balance=balance
        self.minbalance=minbalance


    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance-amount>=self.minbalance:
            self.balance-=amount

        else:
            print("Sorry  Insufficient Balance")


    def printstatement(self):
        print("Account Balane Is:",self.balance)


class Currentaccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,minbalance=1000)

    def __str__(self):
        return"{}'s Current Acc Balance Is:{}".format(self.name,self.balance)


class Savingsaccount(Account):
    def __init__(self,name,balance):
         super().__init__(name,balance,minbalance=0)

         
    def __str__(self):
        return"{}'s Savings Acc Balance Is:{}".format(self.name,self.balance)


obj=Savingsaccount("Rahul",10000)
print(obj)
obj.deposit(5000)
obj.printstatement()
obj.withdraw(10000)
print(obj)
obj.withdraw(6000)
print(obj)
        
        
    
        









  
