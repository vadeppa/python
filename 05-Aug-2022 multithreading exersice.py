'''1. ChildThreadConstructor.py '''


##from threading import *
##class Collage(Thread):
##    def __init__(self):
##        Thread.__init__(self)
##        print("it is parent constructor thread")
##    def run(self):
##        print("it is chaild thread method information")
##obj=Collage()
##obj.start()


'''
2. ChildThreadConstructor. with parameters '''

##from threading import Thread
##
##class University(Thread):
##    def __init__(self,a,b):
##        Thread.__init__(self)
##        print("it is chaild thread parameters:",a,b)
##    def show(self):
##        print("child method threding")
##obj=University(115,111)
##obj.start()
##print("main thread")

'''
3. Creating a thread Without creating a child class to Thread class '''


##from threading import Thread
##
##class Father:
##    def show(self,name,sal):
##        print(name,sal)
##obj=Father()
##t=Thread(target=obj.show, args=('vadeppa',15000))
##t.start()

'''
4. # Single Tasking using a Thread '''

##from threading import Thread

##class Myname:
##    def anysounds(self):
##        self.duck()
##        self.cat()
##        self.dog()
##    def duck(self):
##        print("queck queack")
##    def cat(self):
##        print("mew mew")
##    def dog(self):
##        print("bowe bowe")
##obj=Myname()
##t=Thread(target=obj.anysounds)
##t.start()
        
'''
5.# Multitasking using Multiple Thread '''

##from threading import Thread
##
##class Restarent:
##    def __init__(self,t):
##        self.t=t
##    def Biryani(self):
##        for i in range(1,6):
##            print(self.t,i)
##obj1=Restarent("take order from table:")
##obj2=Restarent("serve order to Table:")
##t1=Thread(target=obj1.Biryani)
##t2=Thread(target=obj2.Biryani)
##
##t1.start()
##t2.start()

'''            
# Multitasking using Multiple Thread '''

##from threading import Thread,current_thread
##
##class Movie(Thread):
##    def __init__(self,available_tickets):
##        self.available_tickets=available_tickets
##    def user(self,need_tickets):
##        self.need_tickets=need_tickets
##        print("available tickes:",self.available_tickets)
##        if(self.available_tickets >= need_tickets):
##            name=current_thread().name
##            print(f'{self.available_tickets} tickets are booked for {name}')
##            self.available_tickets -= need_tickets
##        else:
##            print("sorry ! All tickets are booked")
##obj=Movie(5)
##t1=Thread(target=obj.user,args=(2,),name="Vadeppa")
##t2=Thread(target=obj.user,args=(3,),name="sonu")
##t2.start()
##t1.start()
##            

