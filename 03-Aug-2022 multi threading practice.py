'''
1. MainThread '''

##import threading
##t=threading.current_thread().getName()
##print(t)

'''
2. CreateThreadWithoutClass1 '''

##from threading import Thread
##
##def fun():
##    print("thread running")
##t=Thread(target=fun)
##t.start()

'''
3. Create thread without class2 '''

##from threading import *
##def fun1(a,b):
##    print("thread running:",a,b)
##obj=Thread(target=fun1,args=(100,200))
##obj.start()

'''
4. Create thread without class3 '''

##from threading import Thread
##def show(a,b):
##    print("thread running:",a,b)
##for i in range(5):
##    obj=Thread(target=show,args=(150,250))
##    obj.start()

'''
5. CreateThreadWithoutClass4.'''

##from threading import Thread
##def hello():
##    for i in range(5):
##        print("Child thread")
##obj=Thread(target=hello)
##obj.start()
##for i in range(5):
##    print("main thread")
 
'''
6. SetGetThreadName1. '''

##from threading import Thread,current_thread
##
##def show():
##    print("child threaad",current_thread())
##
##    print("defult child thread name:",current_thread().getName())
##    
##    current_thread().setName("World thread")
##    
##    print("new child thread name:",current_thread().getName())
##
##    current_thread().name='India thread'
##
##    print(current_thread().name)
##    
##obj=Thread(target=show)
##obj.start()
##
##print("hello thread:",current_thread())
##
##print("defualt thread name:",current_thread().getName())
##current_thread().setName("Newdehli thead")
##print("new main thread :",current_thread().getName())
##
##current_thread().name='Telangana'
##print(current_thread().name)

'''
7. SetGetThreadName '''

##from threading import Thread
##def show():
##    pass
##obj=Thread(target=show)
##print(obj.getName())
##
##obj.setName("himalaya")
##print("new child thread name:",obj.getName())
##
##obj.name='kasmir'
##print("update thread name:",obj.name)

'''
8. SetGetThreadName3.py '''

##from threading import Thread
##
##def show(a,b):
##	pass
##    
##obj = Thread(target=show, name='vadeppa')
##print("tne name is:",obj.name)

'''
9. CreateThreadInheritingThreadClass1.py '''

##from threading import Thread
##class Hello(Thread):
##    pass
##obj=Hello()
##print(obj.name)

