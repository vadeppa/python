# pickling method examples

##import pickle
##l=['vadeppa','hari','praveen']
##with open("mom.txt",'wb') as f:
##    pickle.dump(l,f)

# unpickle method

##import pickle
##f= open("mom.txt",'rb')
##emp=pickle.load(f)
##print(emp)
#======================================
##import pickle
##h=(1,2,3,4,5,6)
##with open("histry.txt",'wb')as f:
##    pickle.dump(h,f)
   
##import pickle
##f=open("histry.txt",'rb')
##emp=pickle.load(f)
##print(emp)

#====================================
##import pickle
##d={'v':123,'h':456,'k':456}
##f=open("data.txt",'wb')
##emp=pickle.dump(d,f)
##f.close()

##f=open("data.txt",'rb')
##emp=pickle.load(f)
##print(emp)
##f.close()

#==================================

##import pickle
##
##class Student:
##    def __init__(self,idno,name,sal):
##        self.idno=idno
##        self.name=name
##        self.sal=sal
##    def show(self):
##        print(f"{self.idno},{self.name},{self.sal}")
##obj=Student(22070,'vadeppa',15000)
##
##with open("data.txt",'wb')as f:
##    pickle.dump(obj,f)
##   
##f=open("data.txt",'rb')
##emp=pickle.load(f)
##emp.show()
##f.close()

#===================================
##import pickle
##class University:
##    def __init__(self,sname,sid,scollage):
##        self.sname=sname
##        self.sid=sid
##        self.scollage=scollage
##class Collage(University):
##    
##    def show(self):
##        print(sname,sid,scollage)
##obj=Collage("vadeppa",22070,"sldc")
##with open("show.txt",'wb') as f:
##    pickle.dump(obj,f)
##f=open("show.txt",'rb')
##emp=pickle.load(f)
##emp.show()
##f.close()
        
       
