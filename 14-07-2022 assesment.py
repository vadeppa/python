'''
1. Define a function that accepts roll number and returns whether the student is present or absent.'''

##def student(n):
##    roll_no=int(input("enter a student roll number"))
##    if roll_no in n:
##        print("the student is present")
##    else:
##        print("the student is absent")
##   
##n=[1,2,3,4,5,6,7,8,9,10,11,12]        
##student(n)
        
#output





'''a. Write a python program to print multiple arguments.'''


##def show(*n):
##    for i in n:
##        print(i,end=" ")
##show('a','b','c','k')
##


##output
##
##a, b, c, k,




'''b. Write a function that accepts variable length key value pair as arguments.'''
# 1).

##def show(**n):
##    return n
##print(show(key='vadeppa',key2='chkali',key3='sonu'))

# 2).
##def hello(**k):
##    return k
##print(hello(i='18',j='25'))

#3).
##def name(**l):
##    return l
##print(name(lion="lion",king="king"))


##output
        
##{'key': 'vadeppa', 'key2': 'chkali', 'key3': 'sonu'}       
	
'''3. 	 a. Write a python program to find the power of a number using recursion'''
##
##def power(x,y):
##    if y==0:
##        return 1
##    else:
##        a=x*pow(x,y-1)
##    return a
##x=int(input("enter a number:"))
##y=int(input("enter a number:"))
##print(power(x,y))


##output
##
##enter a number:2
##enter a number:5
##32
##    
        




'''
b. Write a Python program of recursion list sum 
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21'''

##def func(l):
##    sum=0
##    for i in l:
##        if type(i)==type([]):
##            sum+=func(i)
##        else:
##            sum+=i
##    return sum
##print(func([1,2,[3,4],[5,6]]))


'''4. Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it'''

##def outer(a,b):
##    sum=0
##    def inner():
##        sum=a+b
##        return sum
##    return inner()+5
##print(outer(2,3))
##


        

'''5. 	a.  Assign a different name to function and call it through the new name'''

##def show():
##    print("hello good morning vadeppa")
##    
##show2=show
##
##print(show2())



##output


##hello good morning vadeppa

'''
b. 15.Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the
salary is missing in function call it should show it as 9000 '''
##
##def  showEmployee(name,salary=9000):
##    print("the name of the emplyee {} and his salary is {}".format(name,salary))
##    
##showEmployee("vadeppa",15000)
##showEmployee("smith")

##output

##the name of the emplyee vadeppa and his salary is 15000
##the name of the emplyee smith and his salary is 9000



'''
6.	 a. Write a Python function that takes a number as a parameter and check the number is prime or not. '''

##def prime(n):
##    count=0
##    for i in range(1,n+1):
##        if n%i==0:
##            count=count+1
##    if count==2:
##        return True
##    else:
##        return False
##print(prime(9))



           
##output

##False




    
'''
b. Write a Python function that checks whether a passed number is palindrome or not. '''
##
##def pali(n):
##    temp=n
##    x=n[::-1]
##    if x==temp:
##        print("it is palidrome")
##    else:
##        print("it is not a palidrom")
##print(pali('212'))



#output


##it is palindrom

'''
7. 	a. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

##marks=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##marks.sort(key=lambda x:x[1])
##print(marks)


'''
b. 	Write a Python program to create Fibonacci series upto n using Lambda '''

#1).

##list1=[0,1]
##for i in range(10):
##    z=(lambda x:x[-1]+x[-2])
##    list1.append(z(list1))
##print(list1)
##    


#2).

##
##l=[0,1]
##for i in range(15):
##    x=lambda k:k[-1]+k[-2]
##    l.append(x(l))
##print(l)
##

#3).

##k=[0,1]
##for i in range(25):
##    i=lambda i:i[-1]+i[-2]
##    k.append(i(k))
##print(k)



'''c.  Write a Python program to add two given lists using map and lambda.'''

##l1=[1,2,3]
##l2=[1,2,3]
##print(list(map(lambda x,y:x+y,l1,l2)))



#output

#[2, 4, 6]

'''d. Write a Python program to find palindromes in a given list of strings using Lambda.  
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
'''
#1).

##y=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##z=list(filter(lambda y:y==y[::-1],y))
##print(z)
##   

#2).

##x=#y=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']#y=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##y=list(filter(lambda i:i==i[::-1],x))
##print(y)
##

#3).

##z=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##k=tuple(filter(lambda x:x==x[::-1],z))
##print(k)


'''
e. Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.
(Hint: lambda will be passed to sort method's key parameter as argument)'''
#1).

##list1=[9,5,6,4,8,3]
##list1.sort(key=lambda x:-x)
##print(list1)


#2).

##l=[1,2,6,9,8,1,5,6]
##l.sort(key=lambda x:-x)
##print(l)

#3).

##m=[78,95,13,46,89]
##m.sort(key=lambda x:-x)
##print(m)


'''f. Write a lambda function which takes z as a parameter and returns z*11'''


##x=lambda z:z*11
##print(x(9))


##output

##99

'''8. 	a. Using List Comprehension Find all of the numbers from 1–1000 that are divisible by 8 '''


##
##list1=[x for x in range(1,1000) if x%8==0]
##print(list1)
##


#output

##[8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160,
## 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304,
## 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448,
## 456, 464, 472, 480, 488, 496, 504, 512, 520, 528, 536, 544, 552, 560, 568, 576, 584, 592,
## 600, 608, 616, 624, 632, 640, 648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728, 736, 744,
## 752, 760, 768, 776, 784, 792, 800, 808, 816, 824, 832, 840, 848, 856, 864, 872, 880, 888, 896,
## 904, 912, 920, 928, 936, 944, 952, 960, 968, 976, 984, 992]
##

'''
b. Use list comprehension to contruct a new list but add 6 to each item.'''


##list1=[1,2,3,4]
##a=[i+6 for i in list1]
##print(a)


##output


##[7, 8, 9, 10]


'''9. string = "Practice Problems to Drill List Comprehension in Your Head."
Remove all of the vowels in a string (use string above)
Find all of the words in a string that are less than 5 letters (use string above)
Use a dictionary comprehension to count the length of each word in a sentence (use string above) '''

##s="Practice Problems to Drill List Comprehension in Your Head"
##v=['a','e','i','o','u','A','E','I','O','U']
##list1=''
##for i in s:
##    if i not in v:
##        list1+=i
##print(list1)
##
##list2=s.split()
##for i in list2:
##    if len(i)<5:
##        print(i)
##
##x={i:len(i) for i in list2}
##print(x)


##output



##Prctc Prblms t Drll Lst Cmprhnsn n Yr Hd
##to
##List
##in
##Your
##Head
##{'Practice': 8, 'Problems': 8, 'to': 2, 'Drill': 5, 'List': 4, 'Comprehension': 13, 'in': 2, 'Your': 4, 'Head': 4}
##


'''10. First, create a range from 100 to 160 with steps of 10.
Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value.'''

##d={x:x for x in range(100,60,10) if x%100==0}
##print(d)

'''
11. Using dict comprehension and a conditional argument create a dictionary
from the current dictionary where only the key:value pairs with value above 2000
are taken to the new dictionary. dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700} '''

#1).

##dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
##d={i:dict1[i] for i  in dict1 if dict1[i]>2000}
##print(d)

#2).

##d={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
##x={k:d[k] for k in d if d[k]>2000}
##print(x)


#3).

##m={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
##z={g:m[g] for g in m if m[g]>2000}
##print(z)
'''
12. Write a Python Set comprehension with an if clause example
'''
##set1={1,2,3,4,5,6,8}
##even={i for i in set1 if i%2==0}
##print(even)

##output


##{8, 2, 4, 6}











