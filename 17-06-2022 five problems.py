'''
1). WAPP to reverse internal content of every second word present in the
given String.'''

##string='vadeppa chakali madiwal'
##l=string.split()
##list1=[]
##i=0
##while i<len(l):
##    if i%2==0:
##        list1.append(l[i])
##    else:
##        list1.append(l[i][::-1])
##    i=i+1
##    out=' '.join(list1)
##
##print(out)

'''
2) WAPP for the following requirements
    input->a3z2b4
    output->aaabbbbzz(sorted string).'''

##n=input("enter a input:")
##s1=''
##for i in n:
##    if i.isalpha():
##        ch=i
##    else:
##        d=int(i)
##        s1=s1+ch*d
##print(s1)
       
    


'''
3)WAPP  to extract year ,month,date and time using lambda Function.'''

##import datetime
##now = datetime.datetime.now()
##print(now)
##year = lambda x: x.year
##month = lambda x: x.month
##day = lambda x: x.day
##t = lambda x: x.time()
##print(year(now))
##print(month(now))
##print(day(now))
##print(t(now))       
##    

'''
4)WAPP to find the values of length six in given list using lambda Function.'''


##weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
##days = filter(lambda day: day if len(day)==6 else '', weekdays)
##for d in days:
##  print(d)
'''
5)WAPP to find factorial of number using closure Function.'''
##def fun():
##    #fact=1
##    def lis(m):
##        fact=1
##        for i in range(1,m+1):
##            fact=fact*i
##        print(fact)
##    lis(5)
##    
##fun()

import turtle

skk = turtle.Turtle()
for i in range(4):
    skk.forward(50)
    skk.right(90)
turtle.done()


  
