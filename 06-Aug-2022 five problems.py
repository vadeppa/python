'''
1.write a program to count elements in a file? '''

##with open("poem.txt",'r') as f:
##    k=f.read()
##    count=0
##    for i in (k):
##        count+=1
##    print(count)
        
'''
2.write a python program on atleast three magic methods? '''

#abs method

##print(abs(-250))

# __iadd__ method

##n=10
##n+=30
##print(n)

# __round__ method

#print(round(20.6))

'''
3.Write python program on multithreading? '''

##from threading import Thread
##
##class TCS:
##    def __init__(self,name,idno):
##        self.name=name
##        self.idno=idno
##    def show(self):
##        print(f'it is employee name:{self.name}\n it is employee idno:{self.idno}')
##obj=TCS('manasa',22070)
##d=Thread(target=obj.show)
##d.start()



'''
4.Write a dictionary to a file in Python '''
##with open("head.txt",'w+') as f:
##    dict1={'k':10,'b':15,'g':60}
##    f.write(f'{dict1}')
   
##with open("head.txt",'r')as f:
##    d=f.read()
##    print(d)
'''
5.write the program to Get Yesterday’s date using Python? '''

##from datetime import *
##
##today = datetime.today()
##
##yestarday = today - timedelta(days=1)
##print(yestarday)



##from datetime import datetime, timedelta
##today = datetime.today()
##yesterday = today - timedelta(days=1)
##one_week_ago = today - timedelta(days=7)
##thirty_days_ago = today - timedelta(days=30)
##
##print(today)
##print(yesterday)
##print(one_week_ago)
##print(thirty_days_ago)
##
