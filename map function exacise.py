#============================================
# map function examples
#============================================

'''
1.Calculate the length of each word in the tuple:'''


##def lenth(n):
##    return len(n)
##x=map(lenth,("hari","vinu","aksara"))
##print(list(x))


##l=["hari","vinu","aksara"]
##x=list(map(len,l))
##print(x)

'''
2.cancatination two expression'''

##def add(a,b):
##    return a+b
##x=map(add,("hello","hi"),("vadeppa","sonu"))
##print(list(x))


def hello(l):
    x=l[::-1]
    print(x)
k=hello("1234abcd")
print(k)
