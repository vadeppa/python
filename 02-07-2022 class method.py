'''
1.Write a Python class to convert an integer to a roman numeral'''

##class py_solution:
##    def int_to_Roman(self, num):
##        lookup = [
##            (1000, 'M'),
##            (900, 'CM'),
##            (500, 'D'),
##            (400, 'CD'),
##            (100, 'C'),
##            (90, 'XC'),
##            (50, 'L'),
##            (40, 'XL'),
##            (10, 'X'),
##            (9, 'IX'),
##            (5, 'V'),
##            (4, 'IV'),
##            (1, 'I'),
##        ]
##        res = ''
##        for (n, roman) in lookup:
##            (d, num) = divmod(num, n)
##            res += roman * d
##        return res
##print(py_solution().int_to_Roman(5))
##print(py_solution().int_to_Roman(500))
##print(py_solution().int_to_Roman(755))
##print(py_solution().int_to_Roman(1200))
##print(py_solution().int_to_Roman(3456))




'''
2. Write a Python class to convert a roman numeral to an integer.'''

##
##class py_solution:
##    def roman_to_int(self, s):
##        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
##        int_val = 0
##        for i in range(len(s)):
##            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
##                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
##            else:
##                int_val += rom_val[s[i]]
##        return int_val
##
##print(py_solution().roman_to_int('MMMCMLXXXVI'))
##print(py_solution().roman_to_int('MMMM'))
##print(py_solution().roman_to_int('C'))
##

'''
3.Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.'''
##class sol:
##    def valid_parenthese(self,str1):
##        stack,pchar=[],{"(":")","{":"}","[":"]"}
##        for parenthese in str1:
##            if parenthese in pchar:
##                stack.append(parenthese)
##            elif len(stack)==0 or pchar[stack.pop()]!=parenthese:
##                return False
##        return len(stack)==0
##print(sol().valid_parenthese("(){}[]"))
##print(sol().valid_parenthese("()[{(}"))
##print(sol().valid_parenthese("()"))





'''
4.Write a Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]'''

##class sol:
##    def sub_sets(self,set):
##        return self.subsetsrecur([],sorted(set))
##    def subsetsrecur(self,current,set):
##        if set:
##            return self.subsetsrecur(current,set[1:])+self.subsetsrecur(current+[set[0]],set[1:])
##        return [current]
##print(sol().sub_sets([4,5,6]))
    
'''
5.Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.

Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4 '''

##class sol:
##    def pair(sel,num,target):
##        b={}
##        for i, a in enumerate(num):
##            if target-a in b:
##                return(b[target-a],i)
##            b[a]=i
##print(sol().pair((10,20,10,40,50,60,70),50))
##        
    





'''6.Write a Python class to find the three elements that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]'''

##class sol:
##    def sum(self,nums):
##        nums,result,i=sorted(nums),[],0
##        while i<len(nums)-2:
##            j,k=i+1,len(nums)-1
##            while j<k:
##                if nums[i]+nums[j]+nums[k]<0:
##                    j+=1
##                elif nums[i]+nums[j]+nums[k]>0:
##                    k-=1
##                else:
##                    result.append([nums[i],nums[j],nums[k]])
##                    j,k=j+1,k-1
##                    while j<k and nums[j]==nums[j-1]:
##                        j+=1
##                    while j<k and nums[k]==nums[k+1]:
##                        k-=1
##            i+=1
##            while i<len(nums)-2 and nums[i]==nums[i-1]:
##                i+=1
##        return result
##print(sol().sum([-25,-10,-7,-3,2,4,8,10]))
##     




'''
7.Write a Python class to implement pow(x, n).'''
##class sol:
##    def power(self,x,n):
##        if x==0 or x==1 or n==1:
##            return x
##        if x==-1:
##            if n%2==0:
##                return 1
##            else:
##                return -1
##        if n==0:
##            return 1
##        if n<0:
##            return 1/self.power(x,-n)
##        val=self.power(x,n//2)
##        if n%2==0:
##            return val*val
##        return val*val*x
##print(sol().power(2,-3))
##print(sol().power(4,6))
##print(sol().power(10,10))



'''
8.Write a Python class to reverse a string word by word. Go to the editor
Input string : 'hello .py'
Expected Output : '.py hello'''
      
##
##class py_solution:
##    def reverse_words(self, s):
##        return ' '.join(reversed(s.split()))
##
##
##print(py_solution().reverse_words('hello .py'))
##

'''
9.Write a Python class which has two methods get_String and print_String. get_String accept a
string from the user and print_String print the string in upper case.'''
##class sol():
##    def __init__(self):
##        self.str1 = ""
##
##    def get_String(self):
##        self.str1 = input()
##
##    def print_String(self):
##        print(self.str1.upper())
##
##str1 = sol()
##str1.get_String()
##str1.print_String()
##

'''
10.Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
'''
