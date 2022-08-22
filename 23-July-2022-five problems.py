'''
1.Write a Python program to get all possible combinations of the elements of a given list using itertools module.
'''
##from itertools import combinations
##a=[1,2,3,7,4,5,6]
##b=[]
##for i in range(1,len(a)+1):
##    b.append(combinations(a,i))
##
##for i in b:
##    print(list(i))

'''
2.Write a python program to create an iterator that returns consecutive keys and groups from an iterable.
'''
##import itertools
##a="aabbbaaahnnnnjuuuuuuukkkkkklllllgggggggjj"
##grouped=itertools.groupby(a)
##for key,group in grouped:
##    print("key:",key)
##    print("group:",list(group))

'''
3. Write a Python program to find the years where 25th of December be a Sunday between 2000 and 2150.
'''
##from datetime import date
##for y in range(2000,2151):
##    if 6==date(y,12,25).weekday():
##        print(y)

'''
4.write a python program using generator write armstrong.
'''
##def armstrong(num):
##    temp=num
##    sum1=0
##    while num>0:
##        r=num%10
##        sum1=sum1+r**3
##        num=num//10
##    if temp==sum1:
##        yield "Armstrong"
##    else:
##        yield "Not Armstrong"
##num=int(input())
##a=armstrong(num)
##for i in a:
##    print(i)

'''
5.write a python program by using math module use 3 function for each function one example.
'''
##import math
##print(math.sqrt(256))
##print(math.factorial(7))
##print(math.pow(5,4))
