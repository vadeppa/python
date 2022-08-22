'''1.write a program to count number of words and print accending and
desending order
input:this is a mounika and mounika team :
this-1
is-1
a-1
mounika-2
and-1
team-1'''

##string="this is mounika and mounika team"
##l=string.split()
##l1=[]
##
##for i in sorted(l):
##    if i not in l1:
##        l1.append(i)
##        print(i,l.count(i))
##print()
##for i in reversed(sorted(l1)):
##    print(i,l.count(i))


      




'''2.pattern program in the given way?
1
234
56789'''

##num=1
##for x in range(1,6,2):
##   for y in range(x):
##       print(num,end="")
##       num=num+1
##   print()



'''3..find the smallest word in the given sentences and length?
ex:-input:-this is mounika
output:-is -2'''

##a='this is mounika'
##
##s=a.split()
##
##k=min(s)
##print(k,len(k))


'''4.write a multiplication program in the given integer it should be print in 3 alternative order
input:3
output:3x1=3
       3x3=9
       3x5=15'''
##n=3
##for i in range(1,11):
##    if i%2!=0:
##        print(n,"*",i,"=",n*i)
##


'''5. given two strings, name and sport. write a program using string formatting to
concatenate the name followed by message "is playing" and followed by the sport
input: raju
       cricket
output: raju is playing cricket'''


##def play(name,sport):
##    
##    print(name,"is playing",sport)
##    
##play(name='raju',sport='cricket')
