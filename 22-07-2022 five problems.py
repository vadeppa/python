'''
1.Write a Python program to get all possible combinations of the elements of a given list using itertools module.'''
##
##import itertools
##def com(n):
##    tem=[]
##    for i in range(0,len(n)+1):
##        tem.append(tuple(itertools.combinations(n,i)))
##    return tem
##k=[1,2,3,4]
##print("befor combination:")
##print(k)
##print("after combination:")
##print(com(k))






'''
2.Write a python program to create an iterator that returns consecutive keys and groups from an iterable.'''
##
##import itertools 
##l=[1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5]
##obj=itertools.groupby(l)
##for key, group in obj:
##    print('key',key)
##    print('group',list(group))
##    

'''
3. Write a Python program to find the years where 25th of December be a Sunday between 2000 and 2150.'''


##from datetime import date
##def years():
##    for i in range(2000,2151):
##        def isSunday(i):
##            return 6==date(i,12,25).weekday()
##        if isSunday(i):
##            print(i)
##years()



'''
4.write a python program using generator write armstrong.'''

##def Arm():
##    low=int(input("inter a low number:"))
##    high=int(input("Inter a high number"))
##    
##
##    for i in range(low,high+1):
##        t=i
##        s=0
##        m=len(str(i))
##        while(t>0):
##            r=t%10
##            s=s+r**m
##            t=t//10
##        if i==s:
##           yield i
##op=Arm()
##for j in op:
##    print(j)
 
        


    

'''5.write a python program by using math module use 3 function for each function one example.'''

##import math 
##print(math.degrees(80))
##print(math.degrees(90.5))
##
##
##print(math.factorial(4))
##print(math.factorial(5))
##
##print(math.sqrt(25))
##print(math.sqrt(81))
##
##print(math.tan(90))

