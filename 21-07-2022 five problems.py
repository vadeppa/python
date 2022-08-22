'''
1.Write a python program in fibonacci series using generator '''

##def fib(n):
##    a=0
##    b=1
##    for i in range(n):
##        yield a
##        a,b=b,a+b
##for j in fib(10):
##    print(j)
##

 

'''
2.Write a python program to generate the running product of the elemnts of a given iterable '''

##from itertools import accumulate
##import operator
##
##def product(l):
##    return accumulate(l,operator.mul)
##result=product([1,2,3,4])
##for i in result:
##    print(i)

    
'''3.factorial using iterators'''

##n=6
##fact=1
##for i in range(1,n+1):
##    fact=fact*i
##print(fact)

'''4.Write a simple registeration form which contains input buttons heading and radio buttons '''

##from tkinter import *
##
##root=Tk()
##root.title("Apple phone")
##root.geometry('350x200')
##lb=Label(root,text='choose write or wrong',font=("Arial bold",20))
##lb.grid(column=0,row=0)
##bt1=Button(root,text="write",bg='green',font=('Aial bold',20))
##bt=Button(root,text="wrong",bg='red',font=('Arial bold',20))
##bt1.grid(column=0,row=10)
##bt.grid(column=0,row=12)
##
##root.mainloop()


'''5.prime progam using sys module '''

##from sys import *
##
##count=0
##
##for i in range(2,len(ragv)):
##    if (argv[i]%i==0):
##        count=count+1
##if count==2:
##    print("it is prime number")
##else:
##    print("it is not prime number:")
