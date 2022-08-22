#=======================================
# comprehension methods
#=======================================
#1. create a same list

##l1=['a','s','d','f','l','o']
##k=[i for i in l1]
##print(k)

#2.filter the list if the element is 'a'

##l1=['a','b','d','d','a','f']
##k=[i for i in l1 if i!='a']
##print(k)

#3.It makes uppercase the letters

##l1=['a','b','r','g','t','y']
##k=[i.upper() for i in l1]
##print(k)

#4.add the elements

##l1=[i+1 for i in range(20)]
##print(l1)

#5.if else comprehence

##l1=[i if i%2==0 else "invalid" for i in range(20)]
##print(l1)

#6.It makes uppercase the letters except "a"

##l1=['c','d','e','r','a','a']
##k=[i.upper()if i!='a' else i for i in l1]
##print(k)
