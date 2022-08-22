'''
Q1. Write a program in python to replace all word “the” by
another word “them” in a file “poem.txt”. '''

##f=open("poem.txt")
##d=f.read()
##d=d.replace("I","k")
##f.close()
##f=open("poem.txt","w")
##f.write(d)
##f.close()

'''
Q2. Write a program in python to replace a character by another character
in a file “story.txt”. (Accept both the characters from the user) '''


##f=open("poem.txt")
##g=f.read()
##n1=input("enter a charector:")
##n2=input("enter a repaced charector:")
##g=g.replace(n1,n2)
##f.close()
##f=open("poem.txt","w")
##f.write(g)
##f.close()


##f=open("histry.txt",'w+')
##f.write("it is histry of ojas company and it is mistry of the world")
##f.close()
##

'''
Q3. Write a program in python to replace all the ‘a’ by ‘@’ in a file “data.txt”. '''

##f=open("histry.txt",'r')
##k=f.read()
##k=k.replace('a','@')
##f.close()
##f=open("histry,txt","w")
##f.write(k)
##f.close()

'''
Q4. Write a program in python to read file
“data.txt” and display only those lines whose length is more
than 40 characters. '''

##f=open("histry.txt",'r')
##k=f.readlines()
##for i in k:
##    if len(i)>40:
##        print(i)
##f.close()
##

'''
Q5. Write a program in python to remove all duplicate lines from the
file “story.txt”. '''


##f=open("histry.txt",'r')
##m=f.readlines()
##m1=[]
##for i in m:
##    if i not in m1:
##        m1.append(i)
##print(m1)
##f.close()
    
'''
Q6. Write a program in python to display only unique words from the file
“story.txt”.'''

##f=open("histry.txt","r")
##k=f.read()
##k=k.split()
##str1=""
##
##for i in k:
##    if i not in str1:
##        str1=str1+i
##        print(i,end=" ")
##f.close()

'''
Q7. Write a program in python to count the frequency of each vowels in
a file “task.txt”.'''

##f=open("histry.txt",'r')
##k=f.read()
##vowels='aeiouAEIOU'
##count=0
##for i in k:
##    if i in vowels:
##        count=count+1
##print(count)
##f.close()

'''
Q8. Write a program in python to count those words whose length is more than
7 characters in a file “story.txt”.'''

##f=open("histry,txt",'r')
##k=f.read()
##k=k.split()
##count=0
##for i in k:
##    if len(i)>4:
##        count=count+1
##print("the total words are:",count)
##f.close()

'''
Q9. Write a program in python to count those lines from the file “div.txt”
which are starting from ‘T’ or ‘M’.'''

##f=open("histry.txt",'r')
##z=f.readlines()
##count=0
##for i in z:
##    if i[0]=='t' or i[0]=='i':
##        count=count+1
##        print(i)
##print("the number of lines are:",count)
##f.close()

'''
Q10. Write a program in python to count those lines from the file “div.txt”
which are not starting from ‘M’.'''

##f=open("histry.txt",'r')
##b=f.readlines()
##count=0
##for i in b:
##    if i[0]!='i':
##        count=count+1
##print("the not start with :'T' charector is :",i,"\n","the numberof lines are:",count)
##f.close()

'''
Q11. Write a program in python to display those words from a file
“image.txt” which are ending from alphabet ‘m’.'''

##f=open("histry.txt",'r')
##c=f.read()
##c=c.split()
##for i in c:
##    if i[-1]=='d':
##        print(i)
##f.close()

'''
Q12. Write a program in python to read all lines of file “data.txt”
using readline() only.'''

##f=open("histry.txt",'r')
##k=f.readline()
##while k:
##    k=f.readline()
##    print(k,end="")
##f.close()

'''
Q13. Write a program in Python to copy the entire content from file “data.txt”
to “story.txt”'''

##f=open("histry.txt",'r')
##f2=open("mom.txt",'w')
##R=f.read()
##f2.write(R)
##f.close()
##f2.close()

'''
Q14. Write a program in Python to copy the alternate lines from file
“data.txt” to “story.txt”'''

##f=open("mom.txt",'r')
##m1=open("student4.txt",'w')
##k=f.readlines()
##for i in range(len(k)):
##    if i%2==0:
##        m1.write(k[i])
##f.close()
##m1.close()

'''
Q15. Write a program in Python to read the entire content from file
“data.txt” and copy the contents to “story.txt” in upper case. '''

##f=open("mom.txt",'r')
##f2=open("student1.txt",'w')
##d=f.readlines()
##
##for i in d:
##    f2.write(i.upper())
##f.close()
##f2.close()

'''
Q16. Write a program in Python to read the entire content from file
“data.txt” and copy only those words to “story.txt” which start from vowels.'''

##f=open("mom.txt",'r')
##f2=open("student.txt",'w')
##l=f.readlines()
##vowels='aeiouAEIOU'
##for i in l:
##    if i[0] in vowels:
##        f2.write(i)
##f.close()
##f2.close()

'''
Q17. Write a program in Python to read the entire content
from file “data.txt” and copy only those words in separate lines to
“story.txt” which are starting from lower case alphabets .'''

##f=open("mom.txt",'r')
##f2=open("student5.txt",'w')
##d=f.read()
##str1=d.split()
##for i in str1:
##    if i[0].islower():
##        f2.write(i)
##        f2.write("\n")
##        
##f.close()
##f2.close()


'''
Q18. Write a program in Python to read file “data.txt” and copy only
those lines to “story.txt” which are starting from alphabets “A” or “T”.'''

##f=open("mom.txt",'r')
##f2=open("student6.txt",'w')
##d=f.readlines()
##for i in d:
##    if (i[0]=='t' or i[0]=='a'):
##        f2.write(i)
##f.close()
##f2.close()

'''
Q19. Write a program in Python which display the longest word from file
“star.txt”'''

##f=open("mom.txt",'r')
##d=f.read()
##d=d.split()
##l=""
##for i in d:
##    if len(i)>len(l):
##        l=i
##print("longest word:",l)
##f.close()
    
'''
Q20. Write a program in Python which display the longest line from file
“star.txt” '''


##f=open("mom.txt",'r')
##d=f.readlines()
##long=''
##for i in d:
##    if len(i)>len(long):
##        long=i
##print("the longest line is in mom file:",long)
##f.close()


'''
Q21.Write a program in Python to read the file “star.txt” and display the entire content after removing leading and trailing spaces. '''

##f=open("mom.txt",'r')
##d=f.readlines()
##for i in d:
##    print(i.strip())
##f.close()
##

'''        
Q22. Write a program in python that read the content from file “sumit.txt”
and display all numbers. '''

##f=open("mom.txt",'r')
##d=f.read()
##for i in d:
##    if i.isdigit():
##        
##        print(i,end=' ')
##f.close()

'''
Q23. Write a program in Python that display the second and second
last line from the file “life.txt” '''


##f=open("histry.txt",'r')
##d=f.readlines()
##print("the second line is :",d[1])
##print("the second last line is :",d[-2])
##f.close()

'''
Q24. Consider a binary file “data.dat” which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type.
Do the following task in a file
1.Write a function addrec() to add a record in a file.
2.Write a function disp() to display all the records from the file.
3.Write a function specific_disp(room_no) which takes room number as argument and display its details.
4.Write a function mod(room_no) which takes room number as argument and modify it’s details.
5.Write a function del(room_no) which takes room number as argument and delete it’s record from file “data.dat” '''

##import pickle
##def add():
##    list1=[]
##    f=open("hint.dat",'ab')
##    room_num=int(input("enter a room num:"))
##    price=int(input("enter a price:"))
##    room_type=int(input("enter a room_type:"))
##    list1=[room_num,price,room_type]
##    pickle.dump(list1,f)
##    print("Record added in file")
##
##    f.close()
##add()

