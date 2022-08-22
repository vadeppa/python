'''
1)Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

##s='Hello world'
##up=0
##lp=0
##
##for i in s:
##    if i.isupper():
##        up+=1
##    elif i.islower():
##        lp+=1
##    else:
##        pass
##print("UPPER CASE IS:-",up)
##print("LOWER CASE IS:-",lp)
##    
       
'''
2)Python Program to Remove the ith Occurrence of the Given Word in a List.'''
##     
##l=[10,20,30,40,50]
##n=int(input("enter a index position"))
##
##print(l.pop(n))
##print(l)
##



'''3)Python Program to Merge Two Lists and Sort it.'''

##l1=[10,20,40,50,60,90]
##l2=[10,60,40,30,80,70]
##x=l1+l2
##print(sorted(x))
##



'''4)Python Program to Find the Gravitational Force between Two Objects.'''

m1=float(input("enter a m1 value:"))
m2=float(input("enter a m2 value:"))

r=float(input("enter a between center of the massage:"))

G=6.673*(10**-11)
f=(G*m1*m2)/r**2
print("the gravitation force is",round(f,2),"N")


'''5) Write a Python Program for Even Number Pyramid Pattern'''


##n=2
##for x in range(1,5):
##    for y in range(5,x,-1):
##        print(" ",end="")
##    for j in range(0,x):
##        print(str(n)+" ",end="")
##        n+=2
##    print()



