#==============================
#Duck typing method
#==============================
#1.)
##class Dog:
##    def sound(self):
##        print("bowe bowe")
##    def walk(self):
##        print("it is walk")
##class Cat:
##    def sound(self):
##        print("meaw meaw")
##    def walk(self):
##        print(" it is walk")
##class Duck:
##    def sound(self):
##        print("quak quak")
##    def walk(self):
##        print("it is walk")
##def anysound(obj):
##    obj.sound()
##    obj.walk()
##x=Dog()
##y=Cat()
##z=Duck()
##
##anysound(x)
##anysound(y)
##anysound(z)

#2.)

##class India:
##    def capital(self):
##        print('New dehli')
##    def language(self):
##        print("hindi")
##class America:
##    def capital(self):
##        print("wasinton dc")
##    def language(self):
##        print("english")
##a=India()
##b=America()
##l=[a,b]
##def fun(l):
##    for i in l:
##        i.capital()
##        i.language()
##fun(l)

#==================================
# strong typing
#==================================
##class Dog:
##    def sound(self):
##        print("bowe bowe")
##    def walk(self):
##        print("it is walk")
##class Cat:
##    def sound(self):
##        print("meaw meaw")
##    def walk(self):
##        print(" it is walk")
##class Duck:
##    def sound(self):
##        print("quak quak")
##    def walk(self):
##        print("it is walk")
##def anysound(obj):
##    if hasattr(obj,'sound'):
##        obj.sound()
##    if hasattr(obj,'walk'):
##        obj.walk()
##x=Dog()
##y=Cat()
##z=Duck()
##
##anysound(x)
##anysound(y)
##anysound(z)
#==========================
# WrongMethodOverloading
#==========================
# This Method Overloading Concept is not available in Python

##class Teacher:
##    def show(self,a):
##        print("it is Teacher method and:",a)
##    def show(self):
##        print("it is second method")
##obj=Teacher()
##obj.show()
##obj.show(10)

#============================
#method overloading
#============================
##class Collage:
##    def show(self,x=None,y=None,z=None):
##        if x!=None and y!=None and z!=None:
##            R=x+y+z
##            print(R)
##        elif X!=None and y!=None:
##            R=x+y
##            print(R)
##        else:
##            R="please you take at least 2 parameters"
##            print(R)
##obj=Collage()
##obj.show(10,20)
###obj.show()

#===============================
# Method Overriding
#===============================

##class Addition:
##    def show(self,a,b):
##        print("it is addition of two number",a+b)
##class Multiple:
##    def show(self,a,b):
##        print("it is multiple of two numbers",a*b)
##
##obj1=Multiple()
##obj1.show(15,2)
##
##obj1=Addition()
##obj1.show(5,6)

#=====================================
# Method Overriding single inheritance
#=====================================

##class Collage:
##    def show(self,a,b):
##        print("it is addition of two number:",a+b)
##class Student(Collage):
##    def show(self,a,b):
##        super().show(a,b)
##        print("it is mutliple of two number",a*b)
##obj1=Student()
##obj1.show(6,3)


#========================================
#OperatorOverloading
#========================================
##class A:
##	def __init__(self, x):
##		self.x = x
##	def __add__(self, other):
##		return self.x + other.x
##			
##class B:
##	def __init__(self, x):
##		self.x = x
##		
##a = A(100)
##b = B(200)
##print(a+b)		

### importing whole module
##from tkinter import * 
##from tkinter.ttk import *
##  
### importing strftime function to
### retrieve system's time
##from time import strftime
##  
### creating tkinter window
##root = Tk()
##root.title('Clock')
##  
### This function is used to 
### display time on the label
##def time():
##    st = strftime('%H:%M:%S %p')
##    lbl.config(text = st)
##    lbl.after(1000, time)
##  
### Styling the label widget so that clock
### will look more attractive
##lbl = Label(root, font = ('',60, 'bold'),
##            background = 'red',
##            foreground = 'black')
##  
### Placing clock at the centre
### of the tkinter window
##lbl.pack()
##time()
##  
##mainloop()

 

