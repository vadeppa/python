'''
1.Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object. '''

##class Student:
##    def __init__(self,name,age,grade):
##        self.name=name
##        self.age=age
##        self.grade=grade
##
##    def details(self):
##        print(" hello your name ",self.name,"and your",self.age," years old and your grade is",self.grade)
##       
##obj1=Student("omkar",12,"A")
##obj2=Student("ashutosh",14,"A+")
##obj3=Student("sridhar",18,"B+")
##obj1.details()
##obj2.details()
##obj3.details()

'''
2.Write a Program to create an empty valid class by name Students, with no properties. '''



##class Student:
##    def __init__(self):
##        pass
##    def hello(self):
##        print("the class is empty")
##obj1=Student()
##obj1.hello()
##
##
'''
3.Write a program that prints the class name using its object. '''

##class Animal:
##    def __init__(self):
##        pass
##print(Animal().__class__.__name__)

'''4.Write a program, to create a child class Teacher that will inherit the properties of Parent class Staff '''
##class Staff:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    
##    def func1(self):
##        print("the staff name:",self.name)
##        print("the age is name:",self.age)
##class Teacher(Staff):
##    def __init__(self,sub,name,age):
##        self.sub=sub
####        self.name=name
####        self.age=age
##        Staff.__init__(self,name,age)
##    def func2(self):
##        print("the sub is ",self.sub)
##        print("the staff name:",self.name)
##        print("the age is name:",self.age)
##        
##ob=Teacher('maths','vadeppa',24)
##print("the staff is total information:=\n")
##ob.func2()
####ob.func1()

'''
5.Create a Vehicle class without any variables and methods '''
##class Vehicle:
##    pass
##ob=Vehicle()


'''6.Create a child class Bus that will inherit all of the variables and methods of the Vehicle class '''

##class Vehicle:
##    def __init__(self,name,model,price):
##        self.name=name
##        self.model=model
##        self.price=price
##
##    def class1(self):
##        pass
##class Bus(Vehicle):
##    def __init__(self,name,model,price):
##        Vehicle.__init__(self,name,model,price)
##    def class2(self):
##        print("the vehicle details name\n",self.name,"\n",self.model,"\n",self.price)
##ob=Bus("honda",2012,95000)
##ob.class2()
    
        
        

''' 7. Define a property that must have the same value for every class instance (object)'''

##class Company:
##    companyname='honda'
##    def __init__(self): 
##        pass
##class Brand(Company):
##    def __init__(self):
##        pass
##ob=Brand()
##ob=Company()
##
##print(ob.companyname)
##print(ob.companyname)
        




'''
8. Check type of an object '''
##class Hello:
##    pass
##class Hi(Hello):
##    pass
##a=Hello()
##b=Hi()
##print(type(a))
##print(type(b))
##

'''
9.Write a Python program that checks if one class is a subclass of another?'''

##class Master:
##    pass
##class Student(Master):
##    pass
##
##print(issubclass(Student,Master))


'''
10.Determine if School_bus is also an instance of the Vehicle class 
'''
##class Vehicle:
##     def __init__(self):
##         pass
##class School_bus(Vehicle):
##    def __init__(self):
##        pass
##        
##ob=School_bus()
##print(isinstance(ob,Vehicle))
