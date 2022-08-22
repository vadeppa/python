'''
1) write a program on magical method add , pos and neg? '''

# __pos__ method

##class Main:
##    def __init__(self,n):
##        self.n=n
##    def __pos__(self):
##        print(self.n)
##obj=Main(-250)
##+obj


# __neg__ method

##class Main:
##    def __init__(self,m):
##        self.m=m
##    def __neg__(self):
##        print("it is __neg__ value:",self.m)
##obj=Main(250)
##-obj

# __add__ method

##n1=30
##m1=15
##print(n1.__add__(m1))

'''
2) write a program convert day number to date in particular year? '''

##from datetime import datetime
##  
### initializing day number
##day_num = "366"
##  
### print day number
##print("The day number : " + str(day_num))
##  
### adjusting day num
##day_num.rjust(3 + len(day_num), '0')
##  
### Initialize year
##year = "2020"
##  
### converting to date
##res = datetime.strptime(year + "-" + day_num, "%Y-%j").strftime("%m-%d-%Y")
##  
### printing result
##print("Resolved date : " + str(res))

'''
3) write a dictionary to a file in python? '''

##import json
##  
##details = {'Name': "Bob",
##          'Age' :28}
##  
##with open('convert.txt', 'w+') as convert_file:
##     convert_file.write(json.dumps(details))
     




'''
4) find the most repeated word in a text file? '''

##from  collections import *

##with open("poem.txt",'r+')as f:
##    d=f.read()
##    l=[]
##    for i in d.split():
##        l.append(i)
##    k=Counter(l)
##    print(k[keys])
##    
    
            
'''
5) write a program on sprial number?

eg:-1 2 3
    8 9 4
    7 6 5 '''
##for x in range(1,4):
##    for y in range(x):
##        print(y,end="")
##    print()
