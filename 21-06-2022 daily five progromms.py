'''
2.write a program to count number of chareters and print
accending and desendingorderinput:RameshRam
output:a-2,e-1,h-1,m-2,R-2,s-1-assendingdecending:s-1,R-2m-2,,h-1,e-1a-2,'''

from random import randint
number=randint(1,10)
count=0
while count<3:
    chance=int(input("guess the number:"))
    count+=1
    if chance==number:
        print("your guess the currect number:")
        break
    else:
        print("wrong guess try again")

