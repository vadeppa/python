'''
1.. Write a Python program that invoke a given function after specific milliseconds. 
inputs:100ms-16
1000ms-100
2000ms-25100
Sample Output:
Square root after specific miliseconds:
4.0
10.0
158.42979517754858
'''
##from time import sleep
##import math
##def delay(fn,ms,sq):
##    sleep(ms/1000)
##    return fn(sq)
##print(delay(lambda x:math.sqrt(x),100,16))
##print(delay(lambda x:math.sqrt(x),1000,100))
##print(delay(lambda x:math.sqrt(x),2000,25100))

'''
2  we will provide two lists list_1 and list_2.
 The list_1 and list_2 of this function represent the initial list.
 Need to comprehend by list:
1Multiply each value in the two lists separately
2Add each value in the two lists separately
3Multiply the values in the two lists
by using inner and outer functions 
'''
##a=[1,2,3]
##b=[4,5,6]
##mul=list(map((lambda x,y:x*y),a,b))
##print("1.Multiplication:",mul)
##add=list(map((lambda x,y:x+y),a,b))
##print("2.Addition:",add)
##print("Multiplication using inner and outer:")
##def outer(a,b):
##    def inner():
##        mul=list(map((lambda x,y:x*y),a,b))
##        return mul
##    return inner()
##a=outer([1,2,3],[4,5,6])
##print(a)
'''
3.Write a Python program to build a list, using an iterator function and an initial seed value.

1.The iterator function accepts one argument (seed) and must always return a list with two elements ([value, nextSeed]) or False to terminate.
2.Use a generator function, fn_generator, that uses a while loop to call the iterator function and yield the value until it returns False.
3.Use a list comprehension to return the list that is produced by the generator, using the iterator function.
'''
##def unfold(fn, seed):
##  def fn_generator(val):
##    while True: 
##      val = fn(val[1])
##      if val == False: break
##      yield val[0]
##  return [i for i in fn_generator([None, seed])]
##f = lambda n: False if n > 40 else [-n, n + 10]
##print(unfold(f, 10)) 

'''
4.Write a Python program to create Cartesian product of two or more given lists using itertools.
'''
##import itertools
##def cartesian(lists):
##    return list(itertools.product(*lists))
##a=[[1,2],[3,4]]
##print(cartesian(a))
'''
5.Write a Python program to count the frequency of the elements of a given unordered list by using itertools
'''
##from itertools import groupby
##a=[1,2,3,1,2,6,5,4,7,5,9,8,7,2,4,8,5,7,3,1,2,4,6,7,8,3,2,1,8,9,0]
##a.sort()
##print("list:",a)
##result=[len(list(group)) for key, group in groupby(a)]
##print("Frequency:",result)
