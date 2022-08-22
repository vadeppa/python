#====================================================
# lambda function
#====================================================
#syntax:-

'''
lambda arguments:expression '''

##x=lambda a:a+10
##print(x(20))


'''
2.add multiply arguments'''

##x=lambda a,b,c:a+b+c
##print(x(10,20,30))

'''
3.summarize argument '''

##x=lambda a,b,c:a*b*c
##print(x(5,2,3))

'''
Why Use Lambda Functions?'''

##The power of lambda is better shown when you use them as
##an anonymous function inside another function.

##
##def name(n):
##    return lambda a:a*n
##    
'''
3.exampale'''

##def multy(n):
##    return lambda x:x*n
##mul=multy(2)
##print(mul(20))

##def hi(n):
##    return lambda x:x*n
##obj=hi(2)
##print(obj(2))

'''
4.example '''

##def add(n):
##    return lambda a:a*n
##x=add(10)
##y=add(5)
##print(x(50))
##print(y(5))

'''
5.Write a Python program to filter a list of integers using Lambda.'''

##num=[1,2,5,6,32,14,98,2,33,4,3]
##even=list(filter(lambda x:x%2==0,num))
##print(even)
##odd=list(filter(lambda x:x%2!=0,num))
##print(odd)

##l=[1,2,3,4,5,6,45,6,8]
##even=tuple(filter(lambda a:a%2==0,l))
##print(even)


'''
6. Write a Python program to square and cube every number in a given list of
integers using Lambda. '''

##list1=[1,2,3,4,5,6]
##list2=list(map(lambda x:x**2,list1))
##list3=list(map(lambda x:x**3,list1))
##print(list2)
##print(list3)

##l=[1,2,3,4,5,6]
##print(list(map(lambda a:a**2,l)))


'''
7.Write a Python program to find whether a given string starts with
a given character using Lambda.'''

##start=lambda x: True if x.startswith('v') else False
##print(start('vadeppa'))
##print(start("sonu"))

'''8.Write a Python program to find intersection of two given
arrays using Lambda.'''

##list1=[1,2,3,4,50,6,0,40,20,2]
##list2=[1,23,0,50,60,54,5,60,4,6,8]
##result=list(filter(lambda x:x in list1,list2))
##print(result)


