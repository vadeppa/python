from sys import *

#using stdin[standard input]
#=======================
##for i in stdin:
##    if 'v'==i.rstrip():
##        break
##    print(f'input:{i}')
##print("exit")

#======================================================
# using stdout[standard output]
#============================
##stdout.write("hello vadeppa")
##
##stdout.write("this is deviloper")
#========================================================
#using stdrr[standard error stream]

##def show(*k):
##    print(*k,file=stderr)
##print("hi","hello","good morning")
#========================================================
#using path
#======================
##print(path)



#======================================================
#using exit
#===============
##marks=80
##if marks<85:
##    exit("marks less then 85")
##else:
##    print("marks is:",marks)
#===================================================
#using maxsize
#================

##max1=maxsize
##print(max1)

#===============================================
#using maxvalue
#================
##l=[1,2,3,4,6,8,9,77]
##current_max=0
##for i in range(0,len(l)):
##    if l[i]>current_max:
##        current_max=l[i]
##print("the max",(current_max))
##        
#=====================================
# using argv
#=======================
#print("this is the name of the program:",argv[5])

#print("this is the name of the program:",argv[1:])

#======================================================
##sum=0
##for i in range(0,len(argv)):
##    sum+=i
##print("Result:",sum)

#======================================================
##for i in range(1,len(argv)):
##    if int(argv[i])%2==0:
##        print("it is even:",argv[i])
##    else:
##        print("it is odd:",argv[i])
##
#======================================================
##count=0
##for i in range(1,len(argv)):
##    if int(argv[i])%i==0:
##        count=count+1
##if count==2:
##    print("it is prime number:",argv[i])
##else:
##    print("it is not prime number:",argv[i])

#=======================================================
##add=0.0
##for i in range(0,len(argv)):
##    add+=float(i)
##print("the sum of :",add)
##    

#=======================================================
##fact=1
##for i in range(1,len(argv)):
##               fact=fact*argv[i]
##           
##print(fact)


#----------------------------------------------------------------------------
from collections import *
#=============================
##print(Counter(['a','g','t','t','e','i','i','d']))
##
##print(Counter({'v':5,'d':6,'r':8}))
##
##print(Counter(a=3,v=2,k=5))

#=============================================
# OrderedDict
#===============
d={}
d['v']=1
d['a']=2
d['d']=1
d['e']=1
d['p']=2
for key,value in d.items():
    print(key,value)

d=OrderedDict()
d['v']=1
d['a']=2
d['d']=1
d['e']=1
d['p']=2
for key,value in d.items():
    print(key,value)
  
