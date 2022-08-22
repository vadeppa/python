#======================================
#function examples

#======================================
'''2.Write a function called fizz_buzz that takes a number.
-If the number is divisible by 3, it should return “Fizz”.
-If it is divisible by 5, it should return “Buzz”.
-If it is divisible by both 3 and 5, it should return “FizzBuzz”.
-Otherwise, it should return the same number.'''

##def fizz_buzz(n):
##    if n%3==0 and n%5==0:
##        
##        print("Fizz Buzz")
##    elif n%5==0:
##        print("Buzz")
##    elif n%3==0:
##        print("Buzz")
##a=int(input("enter a number:"))  
##fizz_buzz(a)
##    

'''3.Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
-0 EVEN
-1 ODD
-2 EVEN
-3 ODD'''

##def shownumber(limit):
##    for i in range(0,limit+1):
##        if i%2==0:
##            print(i,"even")
##        else:
##            print(i,"odd")
##shownumber(10)

'''4.Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.'''

##def shownumber(limit):
##    for i in range(1,limit+1):
##        if i%5==0 or i%3==0:
##            print(i,end='  ')
##n=int(input("enter a range number:"))            
##shownumber(n)

'''5.Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.'''
##def shownumber(limit):
##    
##    for i in range(0,limit+1):
##        if i>1:
##            for j in range(2,i):
##                if i%j==0:
##                    break
##            else:
##                print(i)
##                
##    
##n=int(input("enter a number:"))    
##shownumber(n)
##            

'''6.Write a function for checking the speed of drivers. This function should have one parameter: speed.
1.If speed is less than 70, it should print “Ok”.
2.Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number
of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
3.If the driver gets more than 12 points, the function should print: “License suspended”'''

##def driver(speed):
##    if speed <70:
##        print("it is ok")
##    elif speed>70:
##        a=speed-70
##        b=a//5
##        if b>12:
##            print("license suspend")
##        else:
##            print(b)
##n=int(input("enter a speed:"))           
##driver(n)
##        

'''9.Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it.
And also it must return both addition and subtraction in a single return '''

##def calculate(x,y):
##    a=x+y
##    b=x-y
##    print("the addition of:",a,"the subtraction:",b)
##    
##    
##calculate(10,5)
##

'''12. Assign a different name to function and call it through the new name'''
##def old_name(n):
##    print(n,"hello wel come to ojas")
##n="vadeppa"    
##new_name=old_name
##new_name(n)

'''13.Generate a Python list of all the even numbers between 4 to 30'''

##def number(n):
##    l=[]
##    for i in range(4,n+1):
##        if i%2==0:
##            l.append(i)
##    print(l)
##number(30)


'''11.Write a recursive function to calculate the sum of numbers from 0 to 10'''

##def num(n):
##    sm=0
##    for i in range(0,n+1):
##        sm+=i
##    print(sm)
##
##num(10)

##def sum1(n):
##    sum=0
##    for i in range(1,n+1):
##        sum+=i
##    print(sum)
##sum1(10)

'''14.Return the largest item from the given list '''
##
##def number(l):
##    print(max(l))
##l=[10,20,30,40,50,60,400]
##number(l)
##    

'''7. What is the result of “bag” > “apple”?'''

##def name(a,b):
##    if a>b:
##        print("it is biggest:",a)
##    else:
##        print("it is biggest:",b)
##a=input("enter a string:")
##b=input("enter b string:")
##name(a,b)

'''8.What is the result of f“{2+2}+{10%3}”?'''

##def result():
##    print(f"{2+2}+{10%3}")
##    
##result()

'''1. What about two asterisks (**)?'''

##def hello(a,b):
##    print(a,b)
##hello(10,20)


'''15.Create a function showEmployee() in such a way that it should accept employee name,
and it’s salary and display both, and if the salary is missing in function call it should show it as 9000'''

##def showemployee(name,salary=9000):
##    print(name)
##    print(salary)
##
##showemployee('vadeppa')
##

##l=[1,2,3,4,5]
##x=list(map(lambda x:x**2,l))
##print(x)
##
##

##x=[1,2,3]
##y=[1,2,3]
##z=[1,2,3]
##print(list(map(lambda i,j,k:i+j+k,x,y,z)))
##l=['hello','good','morning']
##print(list(map(list,l)))


##def sum1(l):
##    if len(l)==1:
##        return l[0]
##    
##    else:
##        return l[0]+sum1(l[1:])
##l=[1,2,3]    
##print(sum1(l))
##        
