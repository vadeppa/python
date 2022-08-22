
##1). Armstrong number
#======================
##def outer(m):
##    def inner():
##        n=int(input("enter a number"))
##        sum1=0
##        k=len(str(n))
##        tem=n
##        while(tem>0):
##            digit=tem%10
##            sum1=sum1+digit**k
##            tem=tem//10
##        if n==sum1:
##            print("it is Armstrong number")
##        else:
##            print("it is Not Armstrong")
##    return inner
##
##def new():
##    print()
##result=outer(new)
##
##result()

##

#2)   even or odd number
#========================            
##def outer(n):
## 
##    def inner():
##        n=int(input("enter a number"))
##        if n%2==0:
##            print("it is even")
##        else:
##            print("it is odd")
##    return inner
##
##def new():
##    pass
##    
##result=outer(new)
##result()

## 3). prime number
#=========================

##def outer(fun):
##    def inner():
##        n=int(input("enter a number"))
##
##        count=0
##        for i in range(1,n+1):
##            if n%i==0:
##                count=count+1
##        if count==2:
##            print("it is prime ")
##        else:
##            print("it is not prime")
##   
##    return inner
##def new():
##    pass
##    
##reult=outer(new)
##reult()

##4). factorial number
#====================

##def outer(fun):
##    def inner():
##        n=int(input("enter a number"))
##
##        fact=1
##        for i in range(1,n+1):
##            fact=fact*i
##        print(fact)
##        
##    return inner
##def new():
##    pass
##    
##reult=outer(new)
##reult()


## 5).odd and even
#======================
##def outer(n):
## 
##    def inner():
##        n=int(input("enter a number"))
##        if n%2!=0:
##            print("it is odd")
##        else:
##            print("it is even")
##    return inner
##
##def new():
##    pass
##    
##result=outer(new)
##result()

#6). porfect number
#===================

##def outer(n):
## 
##    def inner():
##        n=int(input("enter a number"))
##        i=1
##        sum1=0
##        while(i<n):
##            if n%i==0:
##                sum1=sum1+i
##            i=i+1
##        if n==sum1:
##            print("it is perfect number")
##        else:
##            print("it is not perfect number")
##        
##    return inner
##
##def new():
##    pass
##    
##result=outer(new)
##result()

## 7). palindrom number
##======================

##def outer(n):
## 
##    def inner():
##        n=int(input("enter a number:"))
##        tem=n
##        sum1=0
##        while(tem>0):
##            digit=tem%10
##            sum1=sum1*10+digit
##            tem=tem//10
##        if sum1==n:
##            print("it is palindrom")
##        else:
##            print("it is not a palindrom")
##       
##    return inner
##
##def new():
##    pass
##    
##result=outer(new)
##result()

## 8).3.write a python program in strong number using outer and inner function
#========================================
##def outer(k):
##    def inner():
##        n=int(input("enter a number"))
##        temp=n
##        sum1=0
##
##        while(n>0):
##            digit=n%10
##            fact=1
##            for i in range(1,digit+1):
##                fact=fact*i
##
##            sum1=sum1+fact
##            n=n//10
##        if sum1==temp:
##            print("strong number")
##        else:
##            print("not strong number")
##    return inner
##def new():
##    pass
##result=outer(new)
##result()
##
##        
##   


##9).write a python program convert octal to decimalusing outer and inner function 
#=========================

##def outer(n):
## 
##    def inner():
##        n=int(input("enter a number:"))
##        
##        sum1=0
##        i=1
##        while(n):
##            digit=n%10
##        
##            sum1+=digit*i
##            i=i*8
##            n=n//10
##
##        print(sum1)
##       
##    return inner
##
##def new():
##    pass
##    
##result=outer(new)
##result()

##10.write a python program in lcm number using outer and inner function 
#=======================================
##def outer(l):
##    def inner():
##        n1=int(input("enter a number"))
##        n2=int(input("enter a number"))
##        if n1>n2:
##            temp=n1
##        else:
##            temp=n2
##        while(True):
##            if((temp%n1==0) and (temp%n2==0)):
##                lcm=temp
##                break
##            temp+=1
##        print(lcm)
##    
##                
##
##     
##        
##    return inner
##def new():
##    pass
##result=outer(new)
##result()
##



##============with decorator method==============================
#             =====================
#1).even number and odd number
#=====================================
##def outer(j):
##    def inner():
##        n=int(input("enter a number:"))
##        if n%2==0:
##            print("it is even number")
##        else:
##            print("it is odd number")
##    return inner
##@outer
##def new():
##    print()
##
##new()

#2). positve number or nagative number
#===========================================
##def main(l):
##    def inner():
##        n=int(input("enter a number"))
##        if n>0:
##            print("it is pasitive number")
##        else:
##            print("it is nagative number")
##    return inner
##@main
##def new():
##    pass
##new()

#3).prime number
#===============================
##def key(h):
##    def inner():
##        n=int(input("enter a number"))
##        count=0
##        for i in range(1,n+1):
##            if n%i==0:
##                count=count+1
##        if count==2:
##            print("it is prime number")
##        else:
##            print("it is not prime number")
##    return inner
##@key
##def new():
##    pass
##new()


#4)strong number
#==================================
##def value(g):
##    def inner():
##        n=int(input("enter a number"))
##        sum1=0
##        temp=n
##        while(n>0):
##            fact=1
##            digit=n%10
##            for i in range(1,digit+1):
##                fact=fact*i
##            sum1+=fact
##            n=n//10
##        if temp==sum1:
##            print(" it is strong number")
##        else:
##            print("it is not strong number")
##    return inner
##@value
##def new():
##    pass
##new()
##    

# 5).perfect number
#=======================

##def hello(g):
##    def inner():
##        n=int(input("enter a number"))
##        sum1=0
##        i=1
##        while(i<n):
##            
##            if n%i==0:
##                sum1=sum1+i
##            i=i+1
##           
##        if n==sum1:
##            print("it is perfect")
##        else:
##            print("it is not perfect number")
##    return inner
##@hello
##def new():
##    pass
##new()

#6).lcm programm
#======================
##def outer(k):
##    def inner():
##        x=int(input("enter a number"))
##        y=int(input("enter a number"))
##        if x>y:
##            temp=x
##        else:
##            temp=y
##        while(True):
##            if((temp%x==0) and (temp%y==0)):
##                lcm=temp
##                break
##            temp+=1
##        print(lcm)
##    return inner
##@outer
##def new():
##    pass
##new()


#7). octal nuber to desimal number
#==================================

##def outer(n):
## 
##    def inner():
##        n=int(input("enter a number:"))
##        
##        sum1=0
##        i=1
##        while(n):
##            digit=n%10
##        
##            sum1+=digit*i
##            i=i*8
##            n=n//10
##
##        print(sum1)
##       
##    return inner
##@outer
##def new():
##    pass
##new()

#8).Armstrong number
#===========================
##def outer(m):
##    def inner():
##        n=int(input("enter a number"))
##        sum1=0
##        k=len(str(n))
##        tem=n
##        while(tem>0):
##            digit=tem%10
##            sum1=sum1+digit**k
##            tem=tem//10
##        if n==sum1:
##            print("it is Armstrong number")
##        else:
##            print("it is Not Armstrong")
##    return inner
##@outer
##def new():
##    print()
##new()


#9). palindrom number
#===========================

##def outer(n):
## 
##    def inner():
##        n=int(input("enter a number:"))
##        tem=n
##        sum1=0
##        while(tem>0):
##            digit=tem%10
##            sum1=sum1*10+digit
##            tem=tem//10
##        if sum1==n:
##            print("it is palindrom")
##        else:
##            print("it is not a palindrom")
##       
##    return inner
##@outer
##def new():
##    pass
##new()
##


#10). factorial number
#=========================
##def outer(fun):
##    def inner():
##        n=int(input("enter a number"))
##
##        fact=1
##        for i in range(1,n+1):
##            fact=fact*i
##        print(fact)
##        
##    return inner
##@outer
##def new():
##    pass
##new()
##    
