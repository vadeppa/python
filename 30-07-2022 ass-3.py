'''
1.Write a Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] '''

##class Student:
##    def fun(self,a):
##        return self.bb([],sorted(a))
##    def bb(self,c,fun):
##        if fun:
##            return self.bb(c,fun[1:])+self.bb(c+[fun[0]],fun[1:])
##        return [c]
##a=[4,5,3]
##print(Student().fun(a))
##                                               

##output
##[[], [5], [4], [4, 5], [3], [3, 5], [3, 4], [3, 4, 5]]

'''
4.Write a Python program to count the frequency of words in a file '''


##import collections
##with open("mom.txt",'r') as f:
##    d=f.read()
##    print(collections.Counter(d))
##

##import collections
##with open('data.txt','r') as f:
##    r = f.read()
##    print(collections.Counter(r))

##import collections
##with open('data.txt','r') as f:
##    r = f.read()
##    print(collections.Counter(r))


    
##output:

'''
3.Write a Python class which has two methods get_String and print_String. get_String accept a string from the user
and print_String print the string in upper case '''
##
##class string:
##    pass
##
##    def get_string(self):
##        self.str1=input("enter a string:")
##    def print_string(self):
##        print(self.str1.upper())
##        
##obj=string()
##obj.get_string()
##obj.print_string()


'''
6.Write a Python program to generate the running product of the elements of an given iterable. '''
    

'''
5.Write a Python program to extract characters from various text files and puts them into a list. '''


##f=open("mom.txt",'r')
##l=[]
##a=f.readlines()
##for i in a:
##    l.append(i)
##print(l)
##f.close()
'''
In the given Class DateFormatter, implement the method format() such that it accepts the date (date month year),
separated by comma / space or both and return the date in the format of YYYY-MM-DD. 
Eg.: 21,May,2012 / 21 May 2012 / 21, May, 2012 
Output : 2012-05-21 '''
##from datetime import date
##
##class dateformate:
##    def __init__(self,date,month,year):
##        self.date=date
##        self.month=month
##        self.year=year
##    def format(self):
##        print("{}-{}-{}".format(self.year,self.month,self.date))
##        
##obj=dateformate(21,'may',2012)
##obj.format()
##        
        


    

'''
10.Write a python program to find factorial , Fibonacci series, sum of digits, product of digits, reverse of a number, amstrong number.'''

#Fibonacci series


##def outer(k):
##    def inner():
##        a=0
##        b=1
##        for i in range(20):
##            sum=a+b
##            a=b
##            b=sum
##            print("the fibonacci series num are:",b)
##    return inner
##@outer
##def new():
##    pass
##new()


#output

##the fibonacci series num are: 1
##the fibonacci series num are: 2
##the fibonacci series num are: 3
##the fibonacci series num are: 5
##the fibonacci series num are: 8
##the fibonacci series num are: 13
##the fibonacci series num are: 21
##the fibonacci series num are: 34
##the fibonacci series num are: 55

#===================================

#factorial

##def outer(k):
##    def inner():
##        n=int(input("enter a number:"))
##        fact=1
##        for i in range(1,n+1):
##            fact=fact*i
##        print("the factorial of num is:",fact)
##       
##    return inner
##@outer
##def new():
##    pass
##new()

##output

##the factorial of 5 is: 120

#==========================================

#sum of digits

##def outer(k):
##    def inner():
##        n=int(input("enter a number1:"))
##        m=int(input("enter a number2:"))
##        sum=(n+m)
##       
##            
##        print("the sum of ",n,m,"is:",sum)
##       
##    return inner
##@outer
##def new():
##    pass
##new()

#output:

#the sum of  5 5 is: 10

#=======================================
#pruduct of numbera

##def outer(k):
##    def inner():
##        n=int(input("enter a number1:"))
##        m=int(input("enter a number2:"))
##        mul=(n*m)
##       
##            
##        print("the sum of ",n,m,"is:",mul)
##       
##    return inner
##@outer
##def new():
##    pass
##new()
##

##output:

##the sum of  5 6 is: 30

#============================================

#reverse of a number

##def outer(k):
##    def inner(n):
##       
##        temp=n
##        
##        re=''
##        while(n>0):
##            d=n%10
##            re+=str(d)
##            n=n//10
##        print(re)
##        
##    return inner
##@outer
##def new(n):
##    return n
##n=int(input("enter a number1:"))
##new(n)

# output

#351

#========================================

 #Armstrong number

##def outer(k):
##    def inner():
##        n=int(input("enter a number:"))
##       
##        temp=n
##        
##        sum1=0
##        k=len(str(n))
##        while(n>0):
##            d=n%10
##            sum1=sum1+d**k
##            n=n//10
##        if sum1==temp:
##            print("it is Armstrong number:")
##        else:
##            print("it is not Armstrong number;")
##       
##    return inner
##@outer
##def new():
##   pass
##
##new()


##output:
   
##enter a number:153
##it is Armstrong number:

'''The output should contain only vowels and all other characters, including special characters should be filtered out. 
If input is null, return null. 
Example input: “Telephone”, Output: “eeoe” '''
l="Telephone"

##vowels="aeiou"
##for i in l:
##    if i in vowels:
##        print(i,end="")


##vowels="aeiou"
##for i in l:
##    if i in vowels:
##        print(i,end="")


##
##vowels="aeiou"
##for i in l:
##    if i in vowels:
##        print(i,end="")


