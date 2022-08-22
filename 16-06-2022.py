'''1) wap to print range of twin prime numbers by not using function'''

##a=int(input("enter a number:"))
##for i in range(a):
##    if i>1:
##        for j in range(2,i):
##            if i%j==0:
##                break
##        else:
##            x=i+2
##            for k in range(2,x):
##                if x%k==0:
##                    break
##            else:
##                print(i,x)
##        

'''2) wap to print perimutations of the string "abc" by not using function.'''

##a="abc"
##for i in a:
##    for j in a:
##        for k in a:
##            if i!=j and i!=k and j!=k:
##                print(i,j,k)


'''3) wap to print even and odd numbers separatly from a list by using filter function.'''

##l=[12,15,3,65,15,34,9,4,56,5]
##l1=filter(lambda x:x%2==0,l)
##l2=filter(lambda x:x%2!=0,l)
##print(list(l1))
##print(list(l2))
##

'''4) wap to print range of fibonacci series by using recursion function.'''

##def recur_fibo(n):
##   if n <= 1:
##       return n
##   else:
##       return(recur_fibo(n-1) + recur_fibo(n-2))
##
##nterms = 10
##
### check if the number of terms is valid
##if nterms <= 0:
##   print("Plese enter a positive integer")
##else:
##   print("Fibonacci sequence:")
##   for i in range(nterms):
##       print(recur_fibo(i))

'''5) wap to print the strings from a list which are having the length of the list.'''

##
##l=['vadeppa','tharak','ram']
##n=len(l)
##for i in l:
##    if n==len(i):
##        print(i)
##else:
##    print("none")
