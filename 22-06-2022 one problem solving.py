n=[2,3,4]
#print(sorted(n))
l=[]

sum=0
result=0
for i in sorted(n):
 
    sum=sum+i
    l.append(sum)
#print(l)
for i in l:
    result=result+i
result=result-l[0]
print(result)
    
        
  
