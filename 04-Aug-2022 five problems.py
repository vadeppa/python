'''
1) take a list and output has to be repeated of the second half of the list elements
input = [1,2,3,4,5,6]
output = [4,5,6,4,5,6] '''

##l= [1,2,3,4,5,6]
##k=l[3:]
##m=[]
##for i in k:
##    m.append(i)
##for j in k:
##    m.append(j)
##print(m)
    

'''
2) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)'''

##s='vaeH12'
##
##t=''
##for i in s:
##    if i.isnumeric() or i.upper() or i.lower():
##        t=t+i
##        
##if s==t:
##    print("True")
##else:
##    print("False")

'''
3) Write a Python program that matches a string that has an a followed by zero or more b's '''

##import re
##def text_match(text):
##        patterns = '^a(b*)$'
##        if re.search(patterns,  text):
##                return 'Found a match!'
##        else:
##                return('Not matched!')
##print(text_match("ac"))
##print(text_match("abc"))
##print(text_match("a"))
##print(text_match("ab"))
##print(text_match("abb"))

'''
4) Write a Python program that matches a word at the beginning of a string '''

##import re
##def text_match(text):
##        patterns = '^\w+'
##        if re.search(patterns,  text):
##                return 'Found a match!'
##        else:
##                return('Not matched!')
##
##print(text_match("The quick brown fox jumps over the lazy dog."))
##print(text_match(" The quick brown fox jumps over the lazy dog."))

##'''
##5) open a file and enter a lists like each list is having two or more elements in to the file and retrieve their details in the ouput in lists '''
