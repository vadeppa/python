'''
1) wap to create class and create two objects from that class and add those
two objects using _add_ (operator overloading)'''

  
##class Employee:
##    def __init__(self,salary):
##        self.salary=salary
##    def __add__(self,other):
##        return self.salary+other.salary
##    
##e=Employee(15000)
##e1=Employee(10000)
##print(e+e1)

'''
2) wap to create a generator by using send method '''

##def show():
##    while True:
##        n=yield
##        yield n*2
##
##obj=show()
##
##next(obj)
##print(obj.send(10))
##
##next(obj)
##print(obj.send(20))
##
##next(obj)
##print(obj.send(30))

'''
3) wap to create the generator comprehension '''

##l=[1,2,3,4,5,6,7,8,9]
##my=(i**2 for i in l if i%2==0)
##for j in my:
##    print(j)
    

'''
4) print a function n number of times using decorator '''

##def decor(func):
##    def inner():
##        return main()
##    return inner()
##        
##def main():
##    print("hi")
##main()

'''
5) write a python program to check the how many instance variables are
there in a class.'''
##class Father:
##    cn=0
##    def __init__(self):
####        self.name=name
####        self.surname=surname
####        self.age=age
##        Father.cn+=1
##        
##g1=Father()
##g2=Father()
##g3=Father()
##print(Father.cn)

        
