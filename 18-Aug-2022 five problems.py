'''
1).Write a Python program to remove and print every third number from a list of numbers until the list becomes empty '''

##l=[1,2,3,4,5]
##pos=3-1
##index=0
##li=len(l)
##while li>0:
##    index=(pos+index)%li
##    print(l.pop(index))
##    li -=1
##print(l)



'''
2).. Write a Python program to count the number of students of individual class.
Sample Output:
Counter({'VI': 3, 'V': 2, 'VII': 1})  '''

##from collections import Counter
##classes = (
##    ('V', 1),
##    ('VI', 1),
##    ('V', 2),
##    ('VI', 2),
##    ('VI', 3),
##    ('VII', 1),)
##
##print( Counter(i for i,j in classes))





'''
3).Write a Python program to concatenate all elements in a list into a string and return it '''

##l=[1,2,3,4,5,6]
##s=''
##for i in l:
##    s += str(i)
##print(s)






'''
4).Write a Python program to convert a float to ratio. 

Expected Output :

21/5   '''

##from fractions import Fraction
##value = 4.2
##print(Fraction(value).limit_denominator())


'''
5).Write a Python function that prints out the first n rows of Pascal’s triangle '''

##from math import factorial
## 
### input n
##n =int(input("enter a number"))
##for i in range(n):
##    for j in range(n-i+1):
## 
##        # for left spacing
##        print(end=" ")
## 
##    for j in range(i+1):
## 
##        # nCr = n!/((n-r)!*r!)
##        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
## 
##    # for new line
##    print()





   
