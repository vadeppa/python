'''1) write a python program on files to check whether the given file exists or not. 
if it is available then print its content? '''

##import os
##a=os.path.isfile("student1.txt")
##print(a)
##f=open('student1.txt',mode='r')
####f.write("hi myname is vadeppa")
####f.lclose()
##data=f.read()
##print(data)
##f.close()

'''2) Write a Python program to create a file where all letters of English alphabet are listed by specified
number of letters on each line.'''


##number=int(input("Enter  The Number of characters u Want in a Line:"))
##alphabets=""
##for i in range(65,65+26):
##    char=chr(i)
##    alphabets+=char
##f='sample.txt'
##with open(f,"w") as file:
##     modified = [alphabets[i:i + number] +
##                       "\n" for i in range(0, len(alphabets), number)]
##
##     file.writelines(modified)
##
##     print("Successfully Done.")
##    


'''3) Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.'''

##for i in range(65, 65+26):
##    filename = chr(i)+'.txt'
##    with open(chr(i) + ".txt", "w") as file:
##        file.writelines(chr(i))
##

'''4) Write a Python program to interleave multiple lists of the same length. Use itertools module. '''

##import itertools
##
##def interleave(l1,l2,l3):
##    result = list(itertools.chain(zip(l1, l2, l3)))
##    return result
##     
##l1 = [123,143,153,173,183]
##l2 = [100,25,35,69,96]
##l3 = [11,22,33,44,55,66]
##print(interleave(l1,l2,l3))

'''5) Using lambda function print following output.
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz'''

##rs = lambda i: 'FizzBuzz' if i%15 == 0 else 'Fizz' if i%3 == 0 else 'Buzz' if i%5 == 0  else i
##print (list( map ( rs, [ i for i in range( 1,31 )  ]) ) )
##
'''   
5) Using lambda function print following output.
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz'''

##def fun():
##    
##    for i in range(1,31):
##        if i%5==0 and i%3==0:
##            
##            print("fizzbuzz")
##       
##        elif i%3==0:
##            print("fizz")
##        
##        elif i%5==0:
##            print("buzz")
##        
##        
##        else:
##            print(i)
##fun()



