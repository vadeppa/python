#1. How would you confirm that 2 strings have the same identity?

##a=input("enter a string:")
##b=input("enter a string")
##if id(a)==id(b):
##    print("yes")
##else:
##    print("no")
#===================================================
#2. How would you check if each word in a string begins with a capital letter?

##string=input("enter a string:")
##if string.istitle():
##    print("yes")
##else:
##    print("no")

#===================================================
#3. Check if a string contains a specific substrin?

##string=input("enter a string:")
##sub_string=input("enter a substring:")
##if sub_string in string:
##    print("yes cointain sub_string:",sub_string)
##else:
##    print("no not cointain sub_string")

#================================================================
# 4. Find the index of the first occurrence of a substring in a string

##string=input("enter a string:")
##sub_string=input("enter a sub_string:")
##print(string.find(sub_string))


#============================================================
#5. Count the total number of characters in a string?

##string=input("enter a string:")
##print(len(string))

#===================================
#6.Capitalize the first character of a string

##string=input("enter a string:")
##print(string.capitalize())

#==============================================
#7. What is an f-string and how do you use it?

##name="vadeppa"
##age=25
##print(f"hello,my name is {name} and i'am{age} years old")

#====================================================
#8.Check if a string contains only numbers

##string=input("enter a string:")
##if (string.isdigit()):
##    print("yes")
##else:
##    print("no")
#========================================================
#9. Count the number of a specific character in a string

##string=input("enter a string:")"
##count=0
##for i in string:
##    if i=="k":
##        count=count+1
##print(count)
#====================================
#10. Split a string on a specific character

##string=input("enter a string:")
##print(string.split())

#================================
#
#13. Check if a string is composed of all lower case characters

##string=input("enter a string:")
##print(string.lower())
#==================================================
###14. Check if the first character in a string is lowercase

##string=input("enter a string:")
##print(string[0].islower())

##==================================================
#15 Reverse the string “hello world”

##string="hello world"
##print(string.reverse())
#================================

# 18.Check if all characters in a string conform to ASCI#

##string=input("enter a input:")
##print(string.isascii())
#======================================
#19.Uppercase or lowercase an entire string

##string=input("entera a string:")
##print(string.lower())
##print(string.upper())
##=============================================
#20.Uppercase first and last character of a string##

#s=input("enter a string:")
##n=len(s)
##print(s[0].upper()+s[1:n-1]+s[-1].upper())
##
#===================================================
#21.Check if a string is all uppercase

##string=input("enter a string:")
##print(string.isupper())
#=========================================
#17. Join a list of strings into a single string, delimited by hyphens

#print('-'.join(['v','a','d','e','p','p','a']))

#===================================================
#22.Give an example of string slicing
##string=input("enter a string:")
##print(string[:5])
##
##print(string[6:-1])
#=============================================
# Convert an integer to a string
##a=int(input("enter a numer:"))
##print(str(a))
#=========================================================
#25. Check if a string contains only characters of the alphabet

##string=input("enter a string:")
##print(string.isalpha())
#=====================================================
#26. Replace all instances of a substring in a string
##string='hello good morming'
##print(string.replace('hello','hi'))
###==========================================
#27. Return the minimum character in a string
##string=input("enter a string:")
##print(min(string))
###===================================================
#28. Check if all characters in a string are alphanumeric
#string=input("enter a string:")
#print(string.isalnum())
#================================================
#29. Remove whitespace from the left, right or both sides of a string
##string=" hello myname is vadeppa "
##print(string.lstrip())
##print(string.rstrip())
##
##==============================================
#30. Check if a string begins with or ends with a specific character?
##string="vadeppa"
##print(string.startswith('vadeppa'))
##print(string.endswith('vadeppa'))
##=====================================================
