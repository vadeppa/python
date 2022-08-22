'''
1.Python Program to Reverse a Stack using Recursion'''

##class Stack:
##    def __init__(self):
##        self.items = []
## 
##    def is_empty(self):
##        return self.items == []
## 
##    def push(self, data):
##        self.items.append(data)
## 
##    def pop(self):
##        return self.items.pop()
## 
##    def display(self):
##        for data in reversed(self.items):
##            print(data)
## 
##def insert_at_bottom(s, data):
##    if s.is_empty():
##        s.push(data)
##    else:
##        popped = s.pop()
##        insert_at_bottom(s, data)
##        s.push(popped)
## 
## 
##def reverse_stack(s):
##    if not s.is_empty():
##        popped = s.pop()
##        reverse_stack(s)
##        insert_at_bottom(s, popped)
## 
## 
##s = Stack()
##data_list = input('Please enter the elements to push: ').split()
##for data in data_list:
##    s.push(int(data))
## 
##print('The stack:')
##s.display()
##reverse_stack(s)
##print('After reversing:')
##s.display()



'''
2.Python Program to Append the Content of One File to the End of Another File'''

##f=open("poem.txt",'r')
##d=f.read()
##f.close()
##f2=open("head.txt",'a')
##f2.write(d)
##f2.close()



'''
3.Python Program to Create a Class and Get All Possible Distinct Subsets from a Set'''
##class Subset:
##    def f1(self, s1):
##        return self.f2([], sorted(s1))
##
##    def f2(self, curr, s1):
##        if s1:
##            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])
##        return [curr]
##
##
##a = []
##n = int(input("Enter number of elements of list: "))
##for i in range(0, n):
##    b = int(input("Enter element: "))
##    a.append(b)
##print("Subsets: ")
##print(Subset().f1(a))  


'''
4.How can you randomize the items of a list in place in Python? '''

##import random
##l=[1,2,3,6,4,9,8,7]
##print("before",l)
##random.shuffle(l)
##print("After",l)




'''
5.write a python program on showing

KeyboardInterrupt,
ArithmeticError,
StopIteration
AssertionError
ImportError '''

##try:
##    x = input("enter a number")
##    print ('Try using KeyboardInterrupt')
##except KeyboardInterrupt:
##    print ('KeyboardInterrupt exception is caught')
##else:
##    print ('No exceptions are caught')



##import sys
##try:
##    7/0
##except ArithmeticError as e:
##    print(e) 
##    print(sys.exc_type)
##print( 'This is an example of catching ArithmeticError')




'''KeyboardInterrupt'''



##n=int(input("Enter how many number u want to enter:"))
##
##while (True):
##    if n>0:
##        print(n)
##try:
##     raise KeyboardInterrupt
##except KeyboardInterrupt:
##     print("Keyboard interrupt exception caught")



#If the user want to stop the loop use ctrl+c to break then user will get KeyboardInterrupt Error.



'''ArithmeticError'''



##try:
##    value = 12 / 0
##except ZeroDivisionError as e:
##    print(e)



'''StopIteration'''



##mylist = iter(["apple", "banana", "cherry"])
##x = next(mylist)
##print(x)
##x = next(mylist)
##print(x)
##x = next(mylist)
##print(x)
##x=next(mylist)
##print(x)
##


'''ImportError'''
##Raised when a module, or member of a module, cannot be imported.
##There are a few conditions where an ImportError might be raised



##try:
##    from time import datetime
##except Exception as e:
##    print(e)



'''AssertionError'''
##Raised in case of failure of the Assert statement.



##try:
##    x = 1
##    y = 0
##    assert y != 0
##    print(x / y)
##except AssertionError :
##    print("Assertion error occured")
##



from logging import *
basicConfig(filename="logfile4303.log", level=DEBUG, filemode='w', format='%(asctime)s -- %(message)s')
debug("This is Debug")
info("This is Info")
warning("This is Warning")
error("This is Error")
critical("This is Critical")
