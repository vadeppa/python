m=int(input("enter a number:"))
n=int(input("enter a number:"))
diff=0
def prime(x):
    count=0

    for i in range(2,x):
        if x%i==0:
            count=1
            break
    if count==1:
        return 0
    else:
        return 1
if prime(n) and prime(m):
    diff=abs(m-n)
if diff==2:
    print(m,"and",n,"is twin primes")
else:
    print(m,"and",n,"is not prime nummbrs")
#=========================================================
# twin prime numbers in range
'''def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def enter_primes(start,end):
    for i in range(start,end):
        j=i+2
        if prime(i) and prime(j):
            print(i,j,"primes")
enter_primes(2,20)'''
    


    
            
