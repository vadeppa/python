'''1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
##def add(a,b):
##    for i in range(a,b+1):
##        if i%7==0 and (i*5!=0):
##            print(i)
##x=add(2000,3200)
##print(x)


'''2.Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320'''

##n=[1,2,3,4,5,6,7,8]
##
##for i in n:
##    fact=1
##    for j in range(1,i+1):
##        fact=fact*j
##    print(fact,end=" ,")



'''3.With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} '''

##n=[1,2,3,4,5,6,7,8]
##d={}
##for i in n:
##     d1={i:i*i}
##     d.update(d1)
##print(d)
##




'''4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''

##n=input("enter some values: ")
##m=n.split(sep=",")
##
##print(tuple(m))
##print(list(m))

'''5.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''





'''6.Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''
##def func(D):
##    for i in D:
##        C=50
##        H=30
##        q=(2 * C * i)/H
##        q=int(q)
##        print(q)
##        for j in range(q):
##            if j*j>q:
##                print(j-1,end=",")
##                break
##l=100,150,180
##func(l) 
##

'''7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] '''






'''8.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''

##l=input("enter a strings:").split(",")
##em=[]
##for i in l:
##    em.append(i)
##for i in sorted(set(em)):
##    print(i,end=",")
##    
    



'''9.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT'''

##a=input("enter a string:")
##b=input("enter a string:")
##d=a.upper()
##e=b.upper()
##print(d)
##print(e)
##



'''10.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''







'''11.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.'''

##def binary(by):
##    for i in by:
##        rev=i[::-1]
##        k=0
##        dit=0
##        for j in rev:
##            sq=2**k
##            k=k+1
##            if j=="1":
##                dit=dit+sq
##        if dit%5==0:
##            print(i)
##i=["0100","0011","1010","1001"]
##binary(i)
    





'''12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

##def find(a,b):
##    for i in range(a,b+1):
##        cnt=0
##        evn=i
##        while i>0:
##            div=i%10
##            if div%2==0:
##                cnt=cnt+1
##            i=i//10
##        if cnt==len(str(evn)):
##            print(evn,end=",")
##a=int(input("enter a number:"))
##b=int(input("enter a number:"))
##find(a,b)
    



'''13.Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3 '''

##n=input("enter a string")
##dit=0
##alp=0
##for i in n:
##    if i.isdigit():
##        dit+=1
##    elif i.isalpha():
##        alp+=1
##        
##print(dit)
##print(alp)
##       



'''14.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''

##n=input("enter a string:")
##up=0
##lw=0
##for i in n:
##    if i.isupper():
##        up+=1
##    elif i.islower():
##        lw+=1
##    
##print("upper case:",up)
##print("lower case:",lw)
##
##





'''15.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106'''

##a=input()
##k=0
##for i in range(1,5):
##    temp=" "
##    temp=str(a)*i
##    k=k+int(temp)
##print(k)
