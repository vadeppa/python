#Wap sum of two numbers if there sum is less than 10 otherwise print product of number
'''a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=a+b
if c>10:
    print("the sum of ",a,"and",b,"=", c)
else:
    d=a*b
    print("the product of ",a,"and",b,"=",d)'''
#============================================================================
#wap that check if a pearson is eligible to vote ,on the 18 years at least the pearson
'''age=int(input("enter a pearson age:"))
if age<18:
    print("thise pearson is not eligible for vote")
else:
    print("thise pearson is eligible for vote")'''
#==============================================================================
#Armstrong number program
'''a=int(input("enter a number:"))
temp=a
sum=0
x=len(str(a))
while a>0:
    r=a%10
    sum=sum+r**x
    a=a//10
if sum==temp:
    print("it is armstrong number")
else:
    print("it is not armstrong number")'''
#================================================================================
# wap prime number in range
'''n1=int(input("enter a low number:"))
n2=int(input("enter a high number:"))
for i in range(n1,n2+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=" ")'''
#=================================================================================
#wap find the number of  positive or negative ?
'''n=int(input("enter a any number:"))
if n<0:
    print(n,",it is negative number")
else:
    print(n,"it is positive number")'''
#================================================================================
#wap reverse a string
'''string=input("enter a any string:")
reverse=(string[::-1])
print(reverse)'''
#===============================================================================
#wap leap year
'''year=int(input("enter a any year:"))
if (year%400==0)and(year%100==0):
    print(year,"it is leap year")
elif (year%4==0)and(year%100!=0):
    print(year,"it is leap year")
else:
    print(year,"it is not a leap year")'''
#===============================================================================
#WAP to read a single line of and print frist three charector on the given string
'''string=input("enter a any string:")
print(string[:3])'''

#===============================================================================
#WAP to take the number of km as input & convert into mts ?
'''km=int(input("enter a any km:"))
mts=distance*1000
print(mts)
'''
#=============================================================================
#WAP bonus of 5% to an employee if he years of service more than 5 years
'''years=int(input("enter a years:"))
sal=int(input("enter a sal:"))
if years>5:
    print(sal*0.05)
else:
    print("it is not aligible")'''


    

    
