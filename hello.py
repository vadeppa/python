# comprehension methods#
#===============================

# dictionary comprehension
#------------------------------
##key=['a','b','c','d','e']
##values=[1,2,3,4,5]
##dict1={i:j for i,j in zip(key,values)}
##print(dict1)

##
##l=[1,2,3,4]
##dict1={i:i*2 for i in l}
##print(dict1)


##l="hello"
##dict1={i.upper():i*2 for i in l}
##print(dict1)

##x={i:i*3 for i in range(10) if i%2==0}
##print(x)

##l = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
##dict1={i:j for i,j in l.items() if j%2==0}
##print(dict1)


##l = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
##dict1={i:j for i,j in l.items() if j%2==0 if j<40}
##print(dict1)


##l={i:{j:i*j for j in range(6)}for i in range(7)}
##print(l)

# list comprehension
#-----------------------------------------
##l=[1,2,3,4,5,6,7,8,9,10]
##list1=[i for i in l if i%2==0 if i<6]
##print(list1)

##l=[i**2 for i in range(1,10)]
##print(l)

# set comprehension 
#------------------------------------
##l={15,25,61,69}
##set1={i*4 for i in l if i<61}
##print(set1)

#  Array
#==================================
##from array import *
##import datetime
##import pandas
##import IPL



##l=array('i',[12,15,32,45,85])
##for i in l:
##    if i%2==0:
##        print(i)


##l=array('u',['v','e','t'])

#print(dir(array))
#print(dir(datetime))
#print(dir(pandas))
#print(dir(IPL))

##import madule name
##import madule name as aliasname
##from madule name import method1,method2,method3
##from madule name import *

##from k import hello,party
##hello()
##party()

##import k as kit
##from k import hello,party
##party()
from k import *
#hello()
#party()
print(__name__)
print(__doc__)
print(__file__)
