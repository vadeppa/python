'''
1.Write a Python program to read last n lines of a file. '''

##with open("poem.txt",'r')as f:
##    obj=f.readlines()
##    for i in obj[-3::]:
##        print(i)

'''2.Write a Python program to read a file line by line and store it into a list.'''

##with open("poem.txt",'r')as f:
##    li=[i.rstrip() for i in f]
##print(li)
  
    
   
'''3.Write a Python program to read a file line by line store it into a variable. '''

##def fun(fname):
##    with open(fname,'r')as f:
##        data=f.readlines()
##        print(data)
##fun("poem.txt")
  
'''
5. Write a Python program to count the frequency of words in a file '''

##from collections import Counter
##with open("poem.txt",'r')as f:
##    obj=Counter(f.read().split())
##print(obj)

'''
6. Write a Python program to read a random line from a file.'''

##import random
##with open("poem.txt")as f:
##    obj=random.choice(f.read().splitlines())
##print(obj)



'''
7.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.'''

##import string
##
##for letter in string.ascii_uppercase:
##   with open(letter + ".txt", "w") as f:
##       f.writelines(letter)


'''
8.Write a Python program to extract characters from various text files and puts them into a list.'''

##import glob
##l= []
##data = glob.glob("poem.txt")
##for i in data:
##   with open(i,'r') as f:
##       l.append(f.read())
##print(l)


'''
9.Write a Python program that takes a text file as input and returns the number of words of a given text file

Note: Some words can be separated by a comma with no space.'''

##def fun(filepath):
##   with open(filepath) as f:
##       data = f.read()
##       data.replace(",", " ")
##       return len(data.split(" "))
##print(fun("poem.txt"))

