'''
1.write a python program on logging' '''
##from logging import *
##basicConfig(filename="logfile303.log")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")


'''
2.write a python program to remove all the occurances of the given number'''
##l=[1,2,3,4,5,6,67,8,8]
##a=8
##k=[]
##for i in l:
##    if i!=a:
##        k.append(i)
##print(k)


'''
3.write a python program to exact the numbers in a given string and
print sum,minimum and maximum of those numbers
'''
##l=input("enter the string")
##b=[]
##for i in l:
##    if i.isdigit():
##        b.append(int(i))
##print(max(b))
##print(min(b))
##print(sum(b))
        
        


'''
4.write a python program on sprial number 
eg:-9 8 7     
    2 1 6        
    3 4 5'''
##a=int(input("enter the number"))
##
##l=[[0 for i in range(a)] for j in range(a)]
##n=9
##low=0
##high=a-1
##count=int(a+1)//2

##for i in range(count):
##    for j in range(low,high+1):
##        l[i][j]=n
##        n-=1
##    for j in range(low+1,high+1):
##        l[j][high]=n
##        n-=1
##    for j in range(high-1,low-1,-1):
##        l[high][j]=n
##        n-=1
##    for j in range(high-1,low,-1):
##        l[j][low]=n
##        n-=1
##    low+=1
##    high-=1
##    
##for i in range(a):
##    for j in range(a):
##        print(l[i][j],end=" ")
##    print()








'''    
5.create a list of combinations of entered number like below
input: 5
list must be created as [4,4,4,33,33,22,22,1,1,1]'''


##a=int(input("enter tghe number"))
##l=[]
##for i in range(a-1,0,-1):
##    if i==1 or i==a-1:
##        l.append(i)
##        l.append(i)
##        l.append(i)
##    else:
##        l.append(str(i)*2)
##        l.append(str(i)*2)
##print(l)
##        


##n=int(input("enter the number"))
##l=[]
##k=[]
##for i in range(n-1,0,-1):
##    l.append(i)
##d=l[0]
##c=l[-1]
##e=str(d)*3
##q=str(c)*3
##for i in e:
##    k.append(i)
##for i in range(n-2,1,-1):
##    k.append(str(i)*2)
##    k.append(str(i)*2)
##for j in q:
##    k.append(j)
##print(k)
    
