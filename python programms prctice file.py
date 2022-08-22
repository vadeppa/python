
##a=5
##l=[]
##n=0
##p=0
##e=0
##o=0
##z=0
##for i in range(a):
##    b=int(input("enter a number"))
##    l.append(b)
##    i=i+1
##print(l)
##for i in l:
##    if i<0:
##        n+=1
##    elif i==0:
##        z+=1
##    elif i>0:
##        p+=1
##    elif i%2==0:
##        e+=1
##    elif i%2!=0:
##        o+=1
##print("the positive number:",p)
##print("the nagative number:",n)
##print("the odd number:",o)
##print("the even number:",e)
##print("the zero number:",z)
##    
#============================================
##n=input("enter a string:")
##d=[]
##for char in n:
##    if n.count(char)>1:
##        if char not in d:
##            d.append(char)
##                
##print(*d)
#=============================================
def anagram(a,b):
    if sorted(a)==sorted(b):
        return True
    else:
        return False
a=input("enter a string")
b=input("enter a string")
print(anagram(a,b))
