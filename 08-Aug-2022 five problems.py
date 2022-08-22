'''
1) create a nested list by taking list elements from the user like below
[1,2,[3,4],[5,6,7],8,9] '''

##l=[]
##i=0
##while i<=5:
##    a=eval(input("enter a number:"))
##    l.append(a)
##    i+=1
##print(l)
    
'''
2) write a program on to retrieve the data from the file and use seek() and tell() method '''

##with open("poem.txt",'r+') as f:
##   # print(f.tell())
##    #f.write("hello my name is vadeppa")
##    #d=f.read()
##   # print(d)
##    f.seek(0)
##    print(f.readline())
##    

'''
3) write a program on rlock in multithreading '''

##from threading import *
##class ATM:
##    def __init__(self, avl_amt):
##        self.avl_amt=avl_amt
##        self.l=RLock()
##       # print(self.l)
##    def draw(self,need_amt):
##        self.l.acquire()
##       #self.l.acquire()
##       #print(self.l) 
##        print("available balance is :",self.avl_amt)
##        if(self.avl_amt >= need_amt):
##            print("your transaction is successfully:",need_amt)
##            self.avl_amt -= need_amt
##        else:
##            print("sorry !insapisieant balance:")
##        self.l.release()
##        #self.l.release()
##obj=ATM(15000)
##t1=Thread(target=obj.draw,args=(10000,))
##t2=Thread(target=obj.draw,args=(6000,))
##
##t1.start()
##t2.start()
##
##t1.join()
##t2.join()





'''
4) wap to create three functions and three threads for each functions and run those threads '''

##from threading import *
##def show1():
##    print("it is function 1")
##def show2():
##    print("it is function 2")
##def show3():
##    print("it is function 3")
##t1=Thread(target=show1)
##t2=Thread(target=show2)
##t3=Thread(target=show3)
##
##t1.start()
##t2.start()
##t3.start()
##


'''
5) wap to print the next 100th decimal of entered user input 
input = 129, output = 200 , if input = 334, output=400 '''

##n=int(input("Enter a Number:"))
##m=100
##while True:
##    if n<m:
##        print(m)
##        break
##    else:
##        m+=100

