'''
1) Find number of small words in a string and their length?
eg:-This is an offical page
output:- is-2 
         an-2
'''
##st='This is an offical page'.split()
##st1=[]
##
##for i in st:
##    st1.append(len(i))
##m=min(st1)
##for j in (st):
##    if len(j)==m:
##        print(j,len(j))
##        





'''2) Find palindrome in a given string small and large words?
eg:- mom and dad speak malayalam with nitin
mom
dad
malayalam'''

##st='mom and dad speak malayalam with nitin '.split()
##st1=[]
##
##for i in st:
##   if i==i[::-1]:
##       st1.append((len(i),i))
##print(min(st1))
##print(max(st1))
##       
##    



'''
3) Find the digit is binary or not?
eg:-1011
is binary number'''

n=int(input("enter a number:"))

while(n>0):
    j=n%10
    
    if j!=0 and j!=1:
        print("it is not binary")
        break
    n=n//10
    
    if n==0:
        print("it is binary")






'''24:-
its is not a binary 
4)Write a program to print the emojis.
😀
😘
🤗
😪
😷'''

##print("\U0001F600")
##print("\U0001F618")
##print("\U0001F917")
##print("\U0001F62A")
##print("\U0001F637")
##
##



'''5)WAP Login email page ?

example:- email_id='Prudhvi1998@gamil.com'
          password='Rolex123'

if email_id and password True 

output:- prudhvi your email-id successfully open

if email_id or password False

Prudhvi your enter wrong password try agin '''

##n=input("enter your email_id :")
##p=input("enter a your password:")
##
##if n=='vadeppa1994@gmail.com' and p=='vadeppa1994':
##    print("hello your email page is opened")
##else:
##    print("your enter wrong input")
##






