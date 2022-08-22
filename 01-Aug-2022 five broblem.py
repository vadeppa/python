'''
1.write a python program do multiplication program using generators and use sys module to find memory size '''



'''
2..write a python program do multiplication program using function'''

##def fun(n):
##    for i in range(1,11):
##        print(n,"x",i,"=",i*n)
##n=int(input("enter a multipul table name:"))
##fun(n)
    
'''
3.Write a Python program to extract characters from various text files and puts them into a list.'''

##import glob
##l= []
##data = glob.glob("poem.txt")
##for i in data:
##   with open(i,'r') as f:
##       l.append(f.read())
##print(l)


'''
4. Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.'''

##numblines = 5
##alphabets = ""
##for i in range(65, 65+26):
##        charvalue = chr(i)
##        alphabets += charvalue
##filename = 'poem.txt'
##
##with open(filename, "w") as file:
##        modifiedletters = [alphabets[i:i + numblines] + "\n" for i in range(0, len(alphabets), numblines)]
##        file.writelines(modifiedletters)


    



'''5.write a python program in twin prime using outer and inner functions '''


##def prime(n):
##    def twin():
##
##          for i in range(2,n+1):
##              for j in range(2,i):
##                  if i%j==0:
##                      break
##              else:
##                  x=i+2
##                  for k in range(2,x):
##                      if x%k==0:
##                          break
##                  else:
##                      yield (i,x)
##    return twin()
##a=prime(20)
##for i in a:
##    print(i)

#=============================================
