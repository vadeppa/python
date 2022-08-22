## Lock() method
#===================================
# Multitasking using Multiple Thread
# Two Threads acting on same method

##from threading import *
##class Bus:
##    def __init__(self,avl_seat):
##        self.avl_seat=avl_seat
##        self.l=Lock()
##    def reserve(self,need_seat):
##        self.l.acquire(blocking=True)
##        print("available_seats=:",self.avl_seat)
##        if(self.avl_seat >= need_seat):
##            name=current_thread().name
##            print(f'{need_seat} seat is alloted for {name}')
##            self.avl_seat -= need_seat
##        else:
##            print("sorry !   All seats are alloted")
##        self.l.release()
##        
##obj=Bus(3)
##t1=Thread(target=obj.reserve,args=(1,), name="vadeppa")
##t2=Thread(target=obj.reserve,args=(2,),name="Ramu")
##t3=Thread(target=obj.reserve,args=(1,),name='siri')
##
##t1.start()
##t2.start()
##t3.start()
##
##t1.join()
##t2.join()
##t3.join()

## RLock() method
#================================

##from threading import *
##class Train:
##    def __init__(self,avl_seat):
##        self.avl_seat=avl_seat
##        self.l=RLock()
##        #print(self.l)
##    def reserve(self,need_seat):
##        self.l.acquire()
##        self.l.acquire()
##
##        #print(self.l)
##        print("available seats:",self.avl_seat)
##        
##        if(self.avl_seat >= need_seat):
##            name=current_thread().name
##            print(f'{need_seat} seat is alloted for {name}')
##            self.avl_seat -= need_seat
##        else:
##            print("sorry ! All  seats alloted already")
##        self.l.release()
##        self.l.release()
##obj=Train(2)
##t1=Thread(target=obj.reserve,args=(1,),name='vadeppa')
##t2=Thread(target=obj.reserve,args=(1,),name='Eswara manikanta')
##t3=Thread(target=obj.reserve,args=(1,),name="Omkar")
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()
##    
## semaphore method
#==================================
##from threading import *
##class Flight:
##    def __init__(self,avl_seat):
##        self.avl_seat=avl_seat
##        self.l=BoundedSemaphore(3)
##        print(self.l)
##    def reserve(self,need_seat):
##        self.l.acquire()
##        print("available seats:",self.avl_seat)
##        if(self.avl_seat >= need_seat):
##            name=current_thread().name
##            print(f'{need_seat} seats is alloted {name}')
##            self.avl_seat -= need_seat
##        else:
##            print("sorry ! All seat alloted")
##        self.l.release()
##obj=Flight(2)
##t1=Thread(target=obj.reserve,args=(1,),name='Ashuthosh')
##t2=Thread(target=obj.reserve,args=(1,),name='Aksara')
##t3=Thread(target=obj.reserve,args=(1,),name='Anuska')
##t1.start()
##t2.start()
##t3.start()
##
##t1.join()
##t2.join()
##t3.join()

## Dead Lock method
#=============================================

# DeadLock

##from threading import *
##l1 = Lock()
##l2 = Lock()
##
##def bookticket():
##	l1.acquire()
##	print('Bookticket Locked on plan')
##	print('Bookticket wants to lock Class')
##	l2.acquire()
##	print('Bookingticket locked seat')
##	l2.release()
##	l1.release()
##	print('Booking ticket done')
##	
##def cancelticket():
##	l2.acquire()
##	print('cancelticket Locked on Class')
##	print('cancelticket wants to lock Plan')
##	l1.acquire()
##	print('cancelingticket locked seat')
##	l1.release()
##	l2.release()
##	print('canceling ticket done')	
##	
##t1 = Thread(target=bookticket)
##t2 = Thread(target=cancelticket)
##t1.start()
##t2.start()

         
    

