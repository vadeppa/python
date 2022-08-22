'''strings="abcdefghijklmnopqrstuvwxyz"
check_string="i am a repeted in the string"
for char in check_string:
    count=check_string.count(char)
    if count>1:
        print(char,count)'''
#======================================
'''s="andjiopeiutiubo"


for i in s:
    count=s.count(i)
    if count>1:
     
        print(i,count)'''
#========================================
'''s=input("enter a string:")
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    
    print(ch,"is", s.count(ch))

'''
#==========================================
'''st=input("enter a string:")
l=[]

for ch in st:
    if ch not in l:
        l.append(ch)
for ch in reversed(sorted(l)):
      
    print(ch,"is",st.count(ch))'''
#==========================================
'''import collections
str1 = 'hello python as import'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))'''
#======================================
# sum of digit in given string
def sum_digit_string(str1):
    sum_digit=0
    for x in str1:
        if x.isdigit()==True:
            z=int(x)
            sum_digit=sum_digit+z
    return sum_digit
print(sum_digit_string("123456gjduhd5"))




    
    
