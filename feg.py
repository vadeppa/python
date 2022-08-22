


##set1={i for i in range(20)if i%2==0 if i%3==0}
##print(set1)

##s1={i*j for i in range(4,7) for j in range(6,8)}
##print(s1)

##l1=['hero','bajaj','honda']
##l2=[(i,len(i)) for i in l1]
##print(l2)
##
##l1=['a','d','f']
##l2=[i.upper() if i!='a' else i for i in l1]
##print(l2)

##def fact(n):
##    fact1=1
##    for i in range(1,n+1):
##        fact1=fact1*i
##    return fact1
##print(fact(5))
##def fact(n):
##    if(n<=1):
##        return n
##    else:
##        return(fact(n-2)+ fact(n-1))
##n=int(input("enter a number:"))
##for i in range(n):
##    print(fact(i))
##def fibonacci(n):
##    if(n <= 1):
##        return n
##    else:
##        return(fibonacci(n-1) + fibonacci(n-2))
##n = int(input("Enter number of terms:"))
##print("Fibonacci sequence:")
##for i in range(n):
##    print(fibonacci(i))



'''
1.filter the even number '''
##
##l1=(75,20,60,40,3,23,2,50,64)
##print(set(filter(lambda x:x%2==0,l1)))
        # or  #

##lst = (75, 4, 55, 65, 22)
##a = lambda x: x%2==0
##lst = filter(a, lst)
##print(set(lst))

#=====================================================
'''
2. filter the pasitive number '''

##tup=(1,34,-5,0,-77,0.22,33)
##x=lambda a:a>0
##tup=filter(x,tup)
##print(tuple(tup))
##t=(10,20,30,-20,-4,0,9030,-2)
##print(set(filter(lambda x:x>0 ,t)))

'''
3.filter the vowels '''
##
##vow="hello"
##x=lambda a:True if a in "a,e,i,o,u,A,E,I,O,U" else False
##vow=filter(x,vow)
##print(tuple(vow))
''' methods of examples'''

'''static  methods'''
##class Super:
##    x=100
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    @staticmethod
##    def hello():
##        print("it is static method")
##print(Super.hello())
''' class methods'''
##class Hello:
##    def __init__(self):
##        
##        pass
##    classmethod
##    def hi(cls):
##        print("it is class method")
##print(Hello.hi())
