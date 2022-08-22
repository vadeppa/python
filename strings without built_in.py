#1. middle charector of string

##string=input("enter a string:")
##length=len(string)
##middle=length//2
##print(string[middle])

#==================================
#2.half reverse of a string

##string=input("enter astring:")
##length=len(string)
##middle=length//2
##print(string[middle])
##x=string[0:middle]
##y=string[middle:]
##z=y[::-1]
##print(z+x)

#========================================
#3.Remove vowels from text


##vowels='aeiou'
##string=input("enter a string:")
##text=''
##length=len(string)
##for i in range(length):
##    if string[i] not in vowels:
##        text+=string[i]
##print(text)

#===========================
#4.remove extra space from the given string 

##string = "trainee   engeneeir "
##for i in string:
##    if i != " ":
##        print(i,end = "")
##
#===============================
#5.insert string in between a string


##string =input("enter a string:")
##add_string = input( "enter a add string:")
##length=len(string)
##N=length//2
##res =string[:N]+add_string+string[N:]
##print(str(res))

##========================================
#6.Ascii value of a character

##text = input("enter a string:"))
##for char in text:
##    ascii = ord(char)
##    print(char, ":", ascii)
#============================================
#7.number of words in a string

##string=input("enter a string:")
##word=1
##for i in string:
##    if i==" ":
##        word=word+1
##print(word)

#==============================================
#8.place * in front of vowels


##vowels='aeiou'
##string=input('enter a string')
##for i in vowels:
##        string=string.replace(i,'*'+i)
##print(string)

string=input("enter a string:")
print(string.islower())
