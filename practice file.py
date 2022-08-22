
##class Student:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def hello(self):
##        print("it is ",self.name,"iam ",self.age,"years old")
##obj=Student('vadeppa',26)
##obj.hello()

##class Student:
##    def __init__(self):
##        pass
##    def show(self):
##        print("it is hello")
##obj1=Student()
##obj1.show()

##
##class India:
##    def __init__(self):
##        pass
##print(India().__class__.__name__)


##class Student:
##    def __init__(self):
##        pass
##class School(Student):
##    def __init__(self):
##        pass
##obj=School()
##print(issubclass(School,Student))
##print(isinstance(obj,Student))

##class Staff:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def print(self):
##        print("name",self.name,"age",self.age)
##class Teacher(Staff):
##    def __init__(self,sub,name,age):
##        super().__init__(name,age)
##        self.sub=sub
##    def show(self):
##        print("it is ",self.name,"and myage is ",self.age,"my subject is :",self.sub)
##obj=Teacher('maths','vadeppa',26)
##obj.show()
##obj.print()
##        

##
##class vehicle:
##    pass
##obj=vehicle()

##class Vehicle:
##    def __init__(self,tyres,pueal,charges):
##        self.tyres=tyres
##        self.pueal=pueal
##        self.charges=charges
##class Bus(Vehicle):
##    def show(self):
##        print(self.tyres,self.pueal,self.charges)
##obj=Bus("hapolo","deasel",45)
##obj.show()
##    

##class University:
##    x=100
##    def __init__(self):
##        pass
##class Collage(University):
##    def __init__(self):
##        pass
##obj1=Collage()
##
##print(obj1.x)
##

##class A:
##    def __init__(self,name,id):
##        self.name=name
##        self.id=id
##    def show(self):
##        print("the id is :",self.id)
##        print("the name is :",self.name)
##obj=A('vadeppa',200)
###obj.show()
##obj.__setattr__('grade','a')
##k=getattr(obj,'grade')
##print(k)
##


##import types
##def a(x):
##    yield x
##        
##def b(x):
##    return x
##
##def add(x, y):
##    return x + y
##
##print(isinstance(a(456), types.GeneratorType))
##print(isinstance(b(823), types.GeneratorType))
##print(isinstance(add(8,2), types.GeneratorType))

##def fib(num):
##    a = 0
##    b = 1
##    for i in range(num):
##        yield a
##        a, b = b, a + b # Adds values together then swaps them
##
##for x in fib(5):
##    print(x)
##

##import pickle
##class A:
##    def __init__(self,no,name):
##        self.no=no
##        self.name=name
##    def display(self):
##        print(self.no,self.name)
##with open("com.py","wb")as f:
##    obj=A(12,'vadeppa')
##    pickle.dump(obj,f)
##    print("pickling of completed")
##with open ("com.py","rb") as f:
##    pickle.load(f)
##    print("it is unpickling")
##    obj.display()

##class A:
##    def __init__(self):
##        pass
##c=A()
##
##dir(c)

##def div(a,b):
##    def abhi_inner(func):
##        def inner(a,b):
##            if a<b:
##                a,b=b,a
##                return func(a,b)
##        return inner
##obj=abhi_inner(div)
##obj(2,4)


##str1="apple"
##dict={}
##for i in str1:
##    keys=dict.keys()
##    if i in keys:
##        dict[i] += 1
##        
##    else:
##        dict[i]=1
##print(dict)
        
##n=int(input("enter a number:"))
##count=0
##for i in range(1,n+1):
##    if n%i==0:
##        count=count+1
##if count==2:
##    print("it is prime number")
##else:
##    print("it is not prime number:")
        
##s=['helo','myname','is']
##s1=[]
##for i in s:
##    s1.append((len(i),i))
##s1.sort()
##print(s1[-1][1])

##l=[1,2,3,5]
##count=1
##for i in l:
##    count*=i
##print(count)

##l=[12,1,2,5,9]
##count=l[0]
##for i in l:
##    if i>count:
##        count=i
##print(count)

##s='ojas innoovaties'
##d=[]
##for i in s:
##    keys=d.append(i)
##    if i in keys:
##        d[i]+=1
##    else:
##        d[i]=1
##
##print(d)

##a=(10,20,30,40)
##c=" "
##b=c.count(a)
##print(max(a))
##print(count(a))
##print(b)
##b=a.count(20)
##print(b)


'''string="priya"
dict1=[]
for i in string:
    a=dict1.append(i)
    if i in a:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)'''


##a="priyaa"
##for i in a:
##    c=a.count(i)
##    print(c,i)

##
##p = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
##          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
##print(p.keys())
##print(p.values())
##a=10
##b=complex(a)
##print(type(b))
##n=5
##for i in range(1,n):
##    for j in range(n+i):
##        print(j)


##a=10
##b=0
##try:
##    c=a/b
##    print(c)
##    print("try block")
##except ZeroDivisionError:
##    print("not allowed")
##else:
##    print("else")
##finally:
##    print("finally")
    

##import re
##s="Eello:12 Howredy:34."
##p='\d+'
##e=re.findall(p,s)
##print(e)

s="hello"
r="".join(reversed(s))
print(r)
