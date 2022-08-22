'''
1.How do you print duplicate characters from a string?'''

##string='hahbb'
##dup=[]
##for char in string:
##    if string.count(char)>1:
##        if char not in dup:
##            dup.append(char)
##print(*dup)            
##        
'''
2.How do you check if a string contains only digits?'''

##ini_string1=input("enter a string")
##try:
##    num = int(ini_string1)
##    print ("String1 contains only digits")
##except:
##    print ("String1 doesn'tcontains only digits")
##
'''3.Check if the string is anagram or not , if not make it anagram.'''

##a=input("enter a string:")
##b=input("enter a string:")
##if sorted(a)==sorted(b):
##    print("anagram")
##else:
##    print("not anagram")


'''
4.How do you remove a given character from String? '''
##a=input('enter string:')
##b=input('enter a char:')
##c=[]
##d=[]
##for i in a:
##    if i==b:
##        c.append(i)
##    else:
##        d.append(i)
##print(''.join(d))
'''
5.How do you print the first non-repeated character from a string?'''

##a=input()
##b=[]
##c=[]
##for i in a:
##    if i not in b:
##        b.append(i)
##    else:
##        c.append(i)
##print(a)
##print(b)
##print(c)
##for i in b:
##    if i not in c:
##        print(i)
##        break

'''
6.How can a given string be reversed using recursion? '''

##def rev(n):
##    a=n[::-1]
##    return a
##a=input("enter a string:")
##print(rev(a))
##
##keys = ['Ten', 'Twenty', 'Thirty']
##values = [10, 20, 30]
##x=zip(keys,values)
##print(dict(x))
#======================================================================


sample_dict = {"name": "Kelly","age": 25,"salary": 8000,"city": "New york"}

# Keys to extract
keys = ["name", "salary"]

h=



#{'name': 'Kelly', 'salary': 8000}



















