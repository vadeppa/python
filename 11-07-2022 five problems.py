
'''
1). wap take one example duck typing,
 in this methods you must take 3 defferent classes names and in each one class you must take 3 defferent methods '''
##
##class Ojas:
##    def python(self):
##        print("this is Ojas python devoloper")
##    def java(self):
##        print("this is Ojas java devoloper")
##    def devops(self):
##        print("this is Ojas devops devoloper")
##class Infosys:
##    def python(self):
##        print("this is Infosys python devoloper")
##    def java(self):
##        print("this is Infosys java devoloper")
##    def devops(self):
##        print("this is Infosys devops devoloper")
##class Wipro:
##    def python(self):
##        print("thi is Wipro python devoloper")
##    def java(self):
##        print("this is Wipro java devoploper")
##    def devops(self):
##        print("this is Wipro devops devoloper")
##
##obj1=Ojas()
##obj2=Infosys()
##obj3=Wipro()
##k=[obj1,obj2,obj3]
##def company(obj):
##    for i in k:
####        if hasattr(i,'python'):
####            i.python()
####        if hasattr(i,'java'):
####            i.java()
####        if hasattr(i,'devops'):
####            i.devops()
####        
##        i.python()
##        i.java()
##        i.devops()
##          
##x=company(k)
##    
##


'''2). wap take one example wrong method overloding'''
##class Myclass:
##	def sum(self, a):
##		print("1st Sum Method", a)
##		
##	def sum(self):
##		print("2nd Sum Method")		
##		
##obj = Myclass()
##obj.sum()
##obj.sum(10)
##
'''
3). wap solve this pattern

  5 5 5 5 5
   * * * *
    3 3 3 
     * *
      1

      '''

##num=5
##for x in range(num,0,-1):
##    for y in range(num,0,-1):
##        if x>=y:
##            if x%2==0:
##                print("*",end=" ")
##            else:
##                print(x,end=" ")
##        else:
##            print(" ",end="")
##    
##    print()
    
'''
4).wap  take one eaxmple in hierarchical method '''

##class University:
##    def show(self):
##        print("it is university student")
##class Svcollage(University):
##    def show2(self):
##        print("it is svcollage student")
##class Mvcollage(University):
##    def show3(self):
##        print("it is Mvcollage student")
##obj=Svcollage()
##obj2=Mvcollage()
##obj.show()
##obj.show2()
##obj2.show3()
##
'''
5). What is the difference between Python Arrays and lists take one eaxmple ? '''
##import array 
##Ar=array.array('i',[1,2,3,4])
##print(Ar)
##
### OR   #
##
##x=['vadeppa',12,2.3,2j+3]
##print(x)


