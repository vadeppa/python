'''
1.write a python program using oops concept finding prime number or not '''
##class Prime:
##    def __init__(self,num):
##        self.num=num
##    def number(self):
##        count=0
##        for i in range(1,num+1):
##        
##            if num%i==0:
##                count=count+1
##        if count==2:
##            print("it is prime number")
##        else:
##            print("it is not prime number")
##                
##num=int(input("enter a number"))
##obj=Prime(num)
##obj.number()
        

'''
2.write a program on instance method, static method, class method using some examples '''

####instance method
####=======================
##class Master:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def student(self):
##        print("the master name is :",self.name)
##        print("the master age is :",self.age)
##obj=Master("Ramarao",45)
##obj2=Master("Srisailam",50)
##obj.student()
##obj2.student()
##
#### static method
####======================
##class Hello:
##    def __init__(self,name):
##        self.name=name
##    @staticmethod
##    def invite():
##        print("hello good morning")
##    
##print(Hello.invite())
##
####class method
####=========================
##class Master:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    @classmethod
##    def hello(cls):
##        print("hello good aftrnoon")
##print(Master.hello())

'''
3.write a program on single inheritance'''

##class parent:
##    def __init__(self,father,mother):
##        self.father=father
##        self.mother=mother
##    def mom(self):
##     
##        print("my name is :",self.mother,"i am mother to my son")
##        print("my name is :",self.father," ia m father to my son")
##class Child(parent):
##    def son(self):
##        
##        print("iam son of my parents")
##        
##obj=Child('jamulappa','mogulamma')
##obj.mom()
##obj.son()      
##        
##

'''4.write a python program using oops concepts find a fibonacci series'''

##class Fibonaci:
##    def __init__(self,num):
##        self.num=num
##    def result(self):
##        a=0
##        b=1
##        print(a)
##        while b<=num:
##            
##    ## #for i in range(1,num+1):
##            sum1=a+b
##            a=b
##            b=sum1
##            print(sum1)
##num=20            
##obj=Fibonaci(num)
##obj.result()




'''
5.write a python program using oops concepts find armstrong number'''
##class Check:
##    def __init__(self,n):
##        self.n=n
##    def Armstrong(self):
##        temp=self.n
##        sum1=0
##        while temp !=0:
##            r=temp%10
##            sum1+=r**3
##            temp//=10
##        if self.n==sum1:
##            print(self.n,"it is Armstrong number")
##        else:
##            print(self.n,"it is not Armstrong number")
##n=153
##obj=Check(n)
##obj.Armstrong()
##
