#wap right angle tringle with alphabates   print a to e
##n=5
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(chr(64+j),end="")
##              
##    print()

#=============================================================
#wap print strong number given range m to n
##n=int(input("enter a numvber"))
##temp=n
##sum=0
##while(n>0):
##    fact=1
##    digit=n%10
## 
##    for i in range(1,digit+1):
##        fact=fact*i
##    sum=sum+fact
##    n=n//10
##if sum==temp:
##    print("strong number")
##else:
##    print("it not strong number")
#============================================================
#print hollow square
##n=4
##for x in range(1,n+1):
##    for y in range(1,n+1):
##        if((y==1 or y==n)or(x==1 or x==n)):
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()  


#==============================================
# wap print week days using if condition
##n=int(input("enrer a to find a day:"))
##if(n==1):
##    print("monday")
##elif n==2:
##    print("tusday")
##elif n==3:
##    print("wednesady")
##elif n==4:
##    print("thursday")
##elif n==5:
##    print("friday")
##elif n==6:
##    print("saturday")
##elif n==7:
##    print("sunday")
##else:
##    print("your enter more than week number")
#===========================================================
# wap print vowels and consonents given string

##string=input("enter a string:")
##vowel="aeiouAEIOU"
##vow=""
##cons=""
##for i in string:
##    if i in vowel:
##        vow+=i
##    elif i not in vowel:
##        cons+=i
##print("the vowels are:",vow)
##print("the consonents are:",cons)
#====================================================
#perfect number progrpmm

##n=int(input("enter a number"))
##sum=0
##
##for i in range(1,n):
##    if n%i==0:
##        sum+=i
##if sum==n:
##    print("it is perfect number")
##else:
##    print("it is not perfect")
#========================================================    
# wap a string adding hyphen between each charector in word

##string=input("enter a string")
##b=""
##for i in string:
##    b=b+i+"_"
##    #x=b.strip("_")
##print(b)

#============================================================
#wap print each charector of the new line by using while loop

string=input("enter astring:")
b=0
while b<len(string):
    print(string[b])
    b+=1
#==================================================
#find  solid rechtangle using m row and n row columns using * patters

##row=int(input("enter a row number:"))
##col=int(input("enter a colum number:"))
##for i in range(row):
##    for j in range(col):
##        print("*",end=" ")
##    print()
##=====================================================


##row=int(input())
##for i in range(row,0,-1):
##    for j in range(row,i,-1):
##        print(end=" ")
##    for k in range(0,i):
##        print("*",end=" ")
##    print()
##for i in range(0,row):
##    for j in range(0,row-i-1):
##        print(end=" ")
##    for k in range(0,i+1):
##        print("*",end=" ")
##    print()



   


 
