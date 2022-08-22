#==========================================================
# list  methods

#==========================================================

# append method
# 1
'''
name=['vadeppa','tharak','ravindra']
name.append('fariha')
print(name)

'''

# clear method
'''
developers=['pyhon','java','datascience']
developers.clear()
print(developers)

'''

#copy method

'''
a=[1,2,3,4,5]
b=a.copy()
print(b)

'''

#count method

'''
x=[10,20,30,40,50,90,40,60,40,]
y=x.count(40)
print(y)

'''
# extend method
'''
cars=['bmw','benz','hyundai']
bikes=['ktm','honda','hero']
cars.extend(bikes)
print(cars)

'''

#index method
'''
list1=[10,20,30,40,50,60]
x=list1.index(50)
print(x)

'''

#insert method
'''
x=['vadeppa','rakesh','ramu']
x.insert(2,'mommy')
print(x)

'''
# pop method
'''
x=['vadeppa','rakesh','ramu']
x.pop(0)
print(x)

'''
#remove method
'''
list1=[10,20,30,40,20,20,20,50,60]
list1.remove(20)
print(list1)

'''
#revesre method

'''
st=['hi','hello','how']
st.reverse()
print(st)

'''

#sort method

'''
x=[100,30,40,10,400,50]
x.sort()
print(x)

'''
#=============================================================
# tuple  methods
#=============================================================

#count method()
'''
tup=(10,20,30,40,59,10,10,10)
x=tup.count(10)
print(x)

'''

#index method

'''
t=(10,20,30,50,40)
x=t.index(50)
print(x)

'''
# shallow copy
'''
old=[10,20,30,40,50]
new=old
print(old)
print(new)
new[2]=100
print(old)

'''
# shallow nested lis
'''
old=[[10,20,30],[40,50,60],[70,80,90]]
new=old
new[2][1]=500
print(new)
print(old)
print(new)

'''
#==========================================================
#set methods practise

#==========================================================
# add method()
'''
set1={10,20,30,40,50}
set1.add(60)
print(set1)

'''
#clear method()
'''
s={10,20,30,40,50,60,}
s.clear()
print(s)
'''

#copy method()
'''
s={10,40,50,59,90}
s1=s.copy()
print(s1)

'''

#difference method()
'''
set1={10,20,30,40,}
set2={40,30,50,60}
print(set1.difference(set2))

'''

#difference-update method()

'''
s1={10,20,30,40,50}
s2={10,20,40,60,70}
s1.difference_update(s2)
print(s1)

'''
#discard method()
'''
set1={10,20,30,40,50,60,}
set1.discard(60)
print(set1)

'''
#intersection method()
'''
set1={10,20,3,40,50}
set2={10,20,30,60,80}
print(set1.intersection(set2))

'''

#intersection_update method()
'''
set1={10,20,30,40,50}
set2={50,70,80,10,20}
set1.intersection_update(set2)
print(set1)

'''
#disjoint method()
'''
set1={10,20,30,60}
set2={10,20,30,60}
print(set1.isdisjoint(set2))

'''

#issubset method()
'''
set1={1,2,3,4,5,6}
set2={3,4,5}
print(set2.issubset(set1))

'''

#issuperset method()
'''
set1={10,20,30,40,50,60,80}
set2={10,20,30}
print(set1.issuperset(set2))

'''
#pop method()
'''
set1={10,20,30,40,50}
set1.pop()
print(set1)

'''
#remove method()
'''
set1={10,20,30,30,40,40,60,60}
set1.remove(10)
print(set1)

'''

#symmetric_difference method()
'''
set1={10,20,50,70,80}
set2={70,80,90,100}
print(set1.symmetric_difference(set2))


'''
#union method()
'''
set1={10,20,30,40}
set2={10,50,70,80}
print(set1.union(set2))

'''

#update method()
'''
set1={10,20,30,40,50,60}
set2={10,20,60,80,90}
set1.update(set2)
print(set1)

'''

#===========================================================

#DICT METHODS

#===========================================================

#copy method()
'''
dict1={'one':1,'two':2,'three':3}
dict2=dict1.copy()
print(dict2)

'''

#clear method()
'''
dict1={10:1,20:2,30:3,40:5,50:6,60:9}
dict1.clear()
print(dict1)

'''
#fromkeys method()

'''


'''

#get method()
'''

dict1={'hari':10,'vinu':12,'ramu':18}
print(dict1.get('hari'))

'''

#items method()
'''
dict1={'hari':10,'vinu':12,'ramu':18}
dict2=dict1.items()
print(dict2)

'''

#keys methods()
'''

dict1={'hari':10,'vinu':12,'ramu':18}
print(dict1.keys())

'''
#pop method()
'''
dict1={'banana':12,'apple':10,'grapes':20}
dict1.pop('banana')
print(dict1)

'''
#popitem method()
'''

dict1={'banana':12,'apple':10,'grapes':20}
dict1.popitem()
print(dict1)

'''
#setdefault method()
'''
dict1={'a':'1','b':'2','c':'3'}
dict1.setdefault('e')
print(dict1)

'''
#update method()
'''
dict1=['vadeppa','hari','sonu']
values=[27,12,18]
print(dict(zip(dict1,values)))

'''

#values method()

'''
dict1={'hari':12,'vinu':15,'omkar':16}
print(dict1.values())

'''

#==========================================

#string methods

#==========================================

'''1.casefold()method:-it return where all the characters are lower case
it is similar to the lower() method.'''

##a=input("enter the string")
##b=a.casefold()
##print(b)

'''2.capitalize() method:- first character is converted to upper case,
and the rest are converted to lower case'''

##a=input("enter the string")
##b=a.capitalize()
##print(b)

'''3.center() method:- it will center align the string, using specified character
(space id default) as the fill character.
in this
length=required. the length of the returned string
character= optional.the character to fill the missing space on each side
defaolt id " "(space)'''

##first method using space
##a=input("enter the string")
##b=a.center(10)
##print(b)##second method using$
##a=input("enter the string")
##b=a.center(20,"$")
##print(b)

'''4.count() method:- method returns the number of times a specified value
appears in the string'''

##a=input("enter the number")
##b=a.count("a",0,10)
##print(b)

'''5.encode() metthod:-the methods encodes the string, using the specified encoding.
if no encoding is specified, UTF-8 will be used
blackslashreplace:-uses a blacklash instead of the character that could not be encodedignore:-ignores the characters that cannot be encodednamereplace:-replaces the character with a text explaining the characterstrict:-default,raises an error on failurereplace:-replaces the character with a questionmarkxmlcharrefreplace:replaces the character with an xml character
'''
##txt ="My name is Ståle"
##
##print(txt.encode(encoding="ascii",errors="backslashreplace"))
##print(txt.encode(encoding="ascii",errors="ignore"))
##print(txt.encode(encoding="ascii",errors="namereplace"))
##print(txt.encode(encoding="ascii",errors="replace"))
##print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
####txt = "My name is Ståle"
##
##x = txt.encode()
##
##print(x)

'''6.endswith() method:-method returns true if the string ends with the
specified value, otherwise False.parameter values:-
value:-required. the value to check if the string ends with
start:-optional.an integer specifying at which postion to start the search
end:-optional.an integer specifying at which postion to end the search'''

##a=input("enter the string")
##b=a.endswith("tarak")
##print(b)######################
##txt = "Hello, welcome to my world."
##
##x = txt.endswith("my world.", 5, 11)
##
##print(x)

'''7.expandtabs():-expandtabs() method sets the tab size to the specified
number of whitespaces.'''

##txt = "H\te\tl\tl\to"
##
##x = txt.expandtabs(2)
##
##print(x)
##txt = "H\te\tl\tl\to"
##
##print(txt)
##print(txt.expandtabs())
##print(txt.expandtabs(2))
##print(txt.expandtabs(4))
##print(txt.expandtabs(10))

'''8.find() method:-The find() method finds the first occurrence of the specified value.The find() method returns -1 if the value is not found.The find() method is almost the same as the index() method, the only difference is
that the index() method raises an exception if the value is not found.
(See example below)
'''
##txt = "Hello, welcome to my world."
##
##x = txt.find("e")
##
##print(x)
##txt = "Hello, welcome to my world."
##
##x = txt.find("e", 5, 10)
##
##print(x)
##if the given value not in the string means it will give "-1"

'''9.format() method:-method formats the specified value and insert them inside the
string placeholder.the placeholder is defind using curly brackets:{}.format() method returns string.'''

##txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
##txt2 = "My name is {0}, I'm {1}".format("John",36)
##txt3 = "My name is {}, I'm {}".format("John",36)
'''10.format_map():The format_map() method is similar to str.format(**mapping) except
that str.format(**mapping) creates a new dictionary whereas str.format_map(mapping)
doesn't.'''

##point = {'x':4,'y':-5}
##print('{x} {y}'.format(**point))
##
##point = {'x':4,'y':-5, 'z': 0}
##print('{x} {y} {z}'.format_map(point))

'''11.index():-index() method finds the first occurrence of the specified value
the index() method raises an exception if the value is not found.
the index() method is almost the same as the find.only difference is the find() method
returns -1 if the value is not found'''

##txt = "Hello, welcome to my world."
##
##x = txt.index("e")
##
##print(x)

'''12.isalnum():-method returns true if all the characters are alphanumeric'''

##txt = "Company12"
##
##x = txt.isalnum()
##
##print(x)

'''13.isalpha():- method returns true if all the characters are alphabet letters'''

##txt = "Company"
##
##x = txt.isalpha()
##
##print(x)

'''14.isascii():- methods returns if all the characters are ascii characters'''
##txt = "Company12"
##
##x = txt.isalnum()
##
##print(x)

'''15.isdecimal():- method returns true if all the characters are decimals'''

##a = "\u0030" #unicode for 0
##b = "\u0047" #unicode for G
##
##print(a.isdecimal())
##print(b.isdecimal())

'''16.isdigit():- methods returns true if all the characters are digits otherwise false
exponents are also consider as digit'''

##a = "\u0030" #unicode for 0
##b = "\u00B2" #unicode for ²
##
##print(a.isdigit())
##print(b.isdigit())

'''17.isidentifier:-method returns true if the string is a valid identifier,otherwise false'''

##a = "MyFolder"
##b = "Demo002"
##c = "2bring"
##d = "my demo"
##
##print(a.isidentifier()) #true
##print(b.isidentifier()) # true
##print(c.isidentifier()) #false can not start with number
##print(d.isidentifier()) #false can not have space

'''18.islower():-method returns true if all the characters are in lower case, otherwise false
numbers, symbols and spaces are not checked ,only alphabet characters'''

##a = "Hello world!"
##b = "hello 123"
##c = "mynameisPeter"
##
##print(a.islower())
##print(b.islower())
##print(c.islower())

'''19.isnumeric():- method returns true if all the characters are numeric, otherwise false
exponents are also numeric,but -1 and 0.1 are false'''

##a = "\u0030" #unicode for 0
##b = "\u00B2" #unicode for &sup2;
##c = "10km2"
##d = "-1"
##e = "1.5"
##
##print(a.isnumeric())
##print(b.isnumeric())
##print(c.isnumeric())
##print(d.isnumeric())
##print(e.isnumeric())

'''20.isprintable():-methods returns true if all the characters are printable,otherwise false'''

##txt = "Hello!Are you #1?"
##
##x = txt.isprintable()
##
##print(x) we can not use \n statements in this then it will come false

'''21.isspace():-method returns true if all the characters in a string are whitespace
otherwise false'''

##txt = " "
##
##x = txt.isspace()
##
##print(x) ##there will no leters in a string

'''22.istitle():-method returns true if all words in a text start with a upper case letter,
and the rest of the word are lower case letters,otherwise false. symbols and numbers are ignored'''
##a = "HELLO, AND WELCOME TO MY WORLD"
##b = "Hello"
##c = "22 Names"
##d = "This Is %'!?"print(a.istitle())
##print(b.istitle())
##print(c.istitle())
##print(d.istitle())

'''23.isupper():-The isupper() method returns True if all the characters are in upper case,
otherwise False.'''

#txt = "THIS IS NOW!"x = txt.isupper()print(x)

'''24.join():-The join() method takes all items in an iterable and joins them into one string.A string must be specified as the separator.'''

#myTuple = ("John", "Peter", "Vicky")x = "#".join(myTuple)print(x)

'''25.ljust():-The ljust() method will left align the string, using a specified character
(space is default) as the fill character.'''

#txt = "banana"x = txt.ljust(20, "O")print(x)

'''26.lower():-The lower() method returns a string where all characters are lower case. Symbols and Numbers are ignored.'''

#txt = "Hello my FRIENDS"x = txt.lower()print(x)

'''27.lstrip():-The lstrip() method removes any leading characters
(space is the default leading character to remove)'''

#txt = " banana "x = txt.lstrip()print("of all fruits", x, "is my favorite")

'''28.maketrans():-The maketrans() method returns a mapping table that can be used
with the translate() method to replace specified characters.'''

#txt = "Hi maKe!"x = "maKe"
#y = "qist"mytable = txt.maketrans(x, y)print(txt.translate(mytable))

'''29.partition():-The partition() method searches for a specified string, and
splits the string into a tuple containing three elements.'''

#txt = "I could eat bananas all day"x = txt.partition("bananas")print(x)

'''30.replace():-The replace() method replaces a specified phrase with another specified phrase.'''

#txt = "I like bananas"x = txt.replace("bananas", "apples")print(x)

'''31.rfind:-The rfind() method finds the last occurrence of the specified value.The rfind() method returns -1 if the value is not found.The rfind() method is almost the same as the rindex() method.'''txt = "Hello, welcome to my world."x = txt.rfind("e")print(x)


'''
32.rindex():-The rindex() method finds the last occurrence of the specified value.The rindex() method raises an exception if the value is not found.The rindex() method is almost the same as the rfind() method. '''txt = "Hello, welcome to my world."x = txt.rindex("e")print(x)

'''33.rjust():-The rjust() method will right align the string, using a specified
character (space is default) as the fill character.'''

#txt = "banana"x = txt.rjust(20, "O")print(x)

'''34.rpartition():-The rpartition() method searches for the last occurrence
of a specified string, and splits the string into a tuple containing three elements.'''

#txt = "I could eat bananas all day, bananas are my favorite fruit"x = txt.rpartition("apples")print(x)

'''35.rsplit():-The rsplit() method splits a string into a list, starting from the right.If no "max" is specified, this method will return the same as the sp
lit() method.'''

#txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
#x = txt.rsplit(", ", 1)print(x)

'''36.rstrip():-The rstrip() method removes any trailing characters
(characters at the end a string), space is the default trailing character to remove.'''

#txt = "banana,,,,,ssqqqww....."x = txt.rstrip(",.qsw")print(x)

'''37.split():-The split() method splits a string into a list.You can specify the separator, default separator is any whitespace.'''

#txt = "welcome to the jungle"x = txt.split()print(x)

'''38.splitlines():-The splitlines() method splits a string into a list.
The splitting is done at line breaks.'''

#txt = "Thank you for the music\nWelcome to the jungle"x = txt.splitlines(True)print(x)

'''39.startswith():-The startswith() method returns True if the string starts
with the specified value, otherwise False.'''

#txt = "Hello, welcome to my world."x = txt.startswith("Hello")print(x)

'''40.strip():-The strip() method removes any leading (spaces at the beginning)
and trailing (spaces at the end) characters (space is the default leading character to remove)'''

#txt = ",,,,,rrttgg.....banana....rrr"x = txt.strip(",.grt")print(x)

'''41.swapcase():-The swapcase() method returns a string where all the upper case
letters are lower case and vice versa.'''

#txt = "Hello My Name Is PETER"x = txt.swapcase()print(x)

'''42.title():-The title() method returns a string where the first character in
every word is upper case. Like a header, or a title.'''

#txt = "Welcome to my world"x = txt.title()print(x)

'''43.translate():-The translate() method returns a string where some specified characters are
replaced with the character described in a dictionary, or in a mapping table.'''

#txt = "Hello Sam!"
#mytable = txt.maketrans("S", "P")
#print(txt.translate(mytable))

'''44.upper():-The upper() method returns a string where all characters are in upper case. Symbols and Numbers are ignored.'''

#txt = "Hello my friends"x = txt.upper()print(x)

'''45.zfill():- zfill() method adds zeros at the beginning of the sring,until it reaches the specified
length
if the value of the len parameter is lessthan of the string'''

#txt = "50"x = txt.zfill(10)print(x)


