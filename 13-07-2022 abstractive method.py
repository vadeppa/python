# abstract method
#=================================
##from abc import ABC,abstractmethod
##
##class India(ABC):
##    @abstractmethod
##    def state1(self):
##        pass
##    
##   
##    def state2(self):
##        print("hi hello good morning")
##class Telangana(India):
##    
##    def state1(self):
##        pass
##    def state3(self):
##        print("hi every one")
##    def state4(self):
##        print("hello hi")
##    
##    def state5(self):
##        print("it is Tengana state")
##obj=Telangana()
##obj.state4()
##obj.state2()
##obj.state1()
##obj.state5()f
    
# 2).

from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
 
class Pentagon(Polygon):
 
    # overriding abstract method 
    def noofsides(self):
        print("I have 5 sides")
 
class Hexagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
 
class Quadrilateral(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")
    def hello(self):
        print("i have 7 sides")
 
# Driver code
R = Triangle()
R.noofsides()
 
K = Quadrilateral()
K.noofsides()
K.hello()
 
R = Pentagon()
R.noofsides()
 
K = Hexagon()
K.noofsides()

