'''1) wap to print all elements in nested lists as shown in below
l = [1,2,[3,4,[5,6],7],8]
output = 1 2 3 4 5 6 7 8 '''

##l = [1,2,[3,4,[5,6],7],8]
##l2=[]
##def fun(l):
##    for i in l:
##        if type(i) == list:
##            fun(i)
##        else:
##            l2.append(i)
## 
##print('The original list: ', l)
##fun(l)
##print('The list after removing nesting: ', l2)
##
       
  
    


'''
2) Python code to demonstrate working of
 Convert Nested dictionary to Mapped Tuple
Using list comprehension + generator expression

input:
test_dict = {'gfg' : {'x' : 5, 'y' : 6}, 'is' : {'x' : 1, 'y' : 4},
'best' : {'x' : 8, 'y' : 3}}

output:
The grouped dictionary : [(‘x’, (5, 1, 8)), (‘y’, (6, 4, 3))]

3) Convert list of dictionaries to dictionary of lists Using dictionary comprehension.

input:
[{'name': 'sravan', 'subjects': ['java', 'python']},
{'name': 'bobby', 'subjects': ['c/cpp', 'java']},
{'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
{'name': 'rohith', 'subjects': ['php', 'os']},
{'name': 'gnanesh', 'subjects': ['html', 'sql']}]

output:
{'bobby': {'name': 'bobby', 'subjects': ['c/cpp', 'java']},
 'gnanesh': {'name': 'gnanesh', 'subjects': ['html', 'sql']},
 'ojsawi': {'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
 'rohith': {'name': 'rohith', 'subjects': ['php', 'os']},
 'sravan': {'name': 'sravan', 'subjects': ['java', 'python']}}

4) Python  code to demonstrate
# Least Frequent Character in String
The original string is :aaabbbcdddrrreeee
The minimum of all characters in GeeksforGeeks is : c '''

l="aaabbbcdddrrreeee"
l2=""
count=0
for i in l:
    count=count+1
    
  
      




'''
5) wap to modify the existing method in a class after object creation (monkey pacthing)'''

##class University:
##    def collage(self):
##        print("hello this is university")
##    def school(self):
##        print("hello this is school ")
##obj1=University()
##def student(self):
##    print("hi iam student")
##University.student=student
##obj1.student()
##obj1.school()
##obj1.collage()
