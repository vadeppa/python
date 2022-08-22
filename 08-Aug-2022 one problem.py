''' Write a  Python Program using Multithreading ,
Consider a couple who is having a Joint account and both are having their ATM cards.
They come to different ATMs and try to withdraw some amount at the same time.
Let’s say the total balance in the account is 500 and Wife tries to withdraw 450
and the husband tries to withdraw 100. When they swipe the card for withdrawing money,
the balance shown will be 500. Two threads will be created for the transaction,
out of which only one thread should be successful and the other should fail.
If both the threads get successful then its a loss to the bank.
So, the threads should be in synchronization so that one fails and the other wins.'''

##from threading import *
##class Atm:
##    def __init__(self,avl_balance):
##        self.avl_balance=avl_balance
##        self.l=Lock()
##    def Draw(self,need_balance):
##        self.l.acquire()
##        print("your available balance is :",self.avl_balance)
##        if(self.avl_balance >= need_balance):
##            print(f'{need_balance} rupees withdraw')
##            self.avl_balance -= need_balance
##        else:
##            print("sorry ! unsaficiant balance")
##        self.l.release()
##        
##obj=Atm(500)
##t1=Thread(target=obj.Draw,args=(450,))
##t2=Thread(target=obj.Draw,args=(100,))
##
##t1.start()
##t2.start()
##
##t1.join()
##t2.join()
