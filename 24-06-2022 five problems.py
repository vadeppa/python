'''1) write a python program to print string in right angle triangle 
input:python
output:
p
p y
p y t
p y t h
p y t h o
p y t h o n'''


##s='python'
##n=len(s)
##for i in range(1,n+1):
##    for j in range(0,i):
##        print(s[j]+" ",end="")
##    print()
##        


'''2) Write a Python program to split a given dictionary of lists into list of dictionaries.'''
##marks={
##    "Science":[88,89,62,95],
##    "Language":[77,78,84,80]
##    }
##print(marks)
##x=map(dict,zip(*[[(key,val) for val in value]for key,value in marks.items()]))
##print(list(x))
##
##


'''3)WPP to accept student name and marks from the keyboard and creates a dictonary.Also display student marks by taking stundent name as input.'''

##mark={'vadeppa':50,'hari':60,'mani':70}
##a=input("enter a name")
##for key,value in mark.items():
##    if key==a:
##        print(value)




'''4) write a program to print a program like below

          1   
        1   1
      1   2   1
    1   3   3   1
  1   4   4   4   1
1   5   5   5   5   1

'''
##a=int(input())
##s=""
##print((a*"")+"1")
##print(((a-1)*" ")+"1"+" "+"1")
##for i in range(2,a+1):
##    start=((a-i)*" ")
##    nums=(" "+str(i)+" ")*(i-1)
##    s=start+"1 "+nums+"1 "
##    print(s)
##
##




'''5) write a function which is taking another funciton as an argument'''


def fibonacci(a):
    if a<=1:
        return a
    else:
        msg=fibonacci(a-2)+fibonacci(a-1)
    return msg
def fibonacciseries(a):
    list_a=[]
    for i in range(a):
        list_a+=[fibonacci(i)]
    return list_a
a=int(input())
print(fibonacciseries(a))



