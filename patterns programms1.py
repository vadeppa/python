#wap print pattern programm

##for x in range(1,6):
##    for y in range(1,6):
##        print(y,end=" ")
##    print()
#=======================================

#wap programm print pattern

##for x in range(5,0,-1):
##    for y in range(5,0,-1):
##        print(y,end=" ")
##    print()
##
#=======================================
#wap  program print pattern

##for x in range(5,0,-1):
##    for y in range(5,0,-1):
##        print(x,end=" ")
##    print()
#=======================================
#print pattern progromm

##for x in range(1,6):
##     for y in range(1,x+1):
##         print(y,end=" ")
##     print()

#===============================
# wap pattern progromm

##for x in range(1,6):
##    for y in range(1,x+1):
##        print(x,end=" ")
##    print()
#======================================
#wap print patern programm
##num=1
##for x in range(1,6):
##    for y in range(1,x+1):
##        print(str(num)+" ",end="")
##        num+=1
##    print()



#=====================================================
#7.Write a program to print the following Patter

##for x in range(5,0,-1):
##    for y in range(6,x,-1):
##        print(x,end="")
##    print()
##
#=================================================
###8.Write a program to print the following Pattern
##num=1
##for x in range(1,5):
##    for y in range(1,x+1):
##        print(str(num)+"",end="")
##        num+=1
##    print()
##
###===============================================
###9.Write a program to print the following Pattern

##n=5
##ch=0
##for x in range(1,n+1):
##    for y in range(1,x+1):
##        print(chr(ch+65)+"",end="")
##        if ch<26:
##            ch+=1
##        else:
##            ch=0
##    print()
#========================================
#10.Write a program to print the following Pattern

##for x in range(1,6):
##    for y in range(1,6):
##        print("*",end=" ")
##    print()
##    

#================================================
#11.Write a program to print the following Pattern
##for x in range(1,6):
##    for y in range(1,x+1):
##        print("*",end=" ")
##    print()

#====================================
###12.Write a program to print the following Pattern
##n=5
##for x in range(1,n+1):
##    for y in range(1,n+1):
##        if(y==1 or y==n)or(x==1 or x==n):
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()
##======================================================
##n
##n=5
##for x in range(n,0,-1):
##    for y in range(1,n+1):
##        if x<=y:
##            if x%2==0:
##                print("*",end="")
##            else:
##                print("*",end="")
##        else:
##            print("",end="")
##    print()
#===============================
#14.Display Multiplication Table in given range using Nested for loops


##a=int(input("enter a number:"))
##b=int(input("enter a number:"))
##
##for i in range(a,b+1):
##    for j in range(1,b+1):
##        print(i,"*",j,"=",i*j)
##    print()

#================================
#15.prime numbers given range
##a=int(input())
##b=int(input())
##for i in range(a,b):
##    if i>1:
##        for j in range(2,i):
##            if i%j==0:
##                break
##        else:
##            print(i,end=" ")
##==================================
#
##num=10
##for i in range(4):
##    space="   "*i
##    print(space,end="")
##    for j in range(4-i):
##        print(num,end=" ")
##        num-=1
##    print()
