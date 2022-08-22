'''
Using functools write a program on partialmethod,lru_cache and total_ordering
'''
##from functools import partial
##def add(a,b,c):
##    return 100*a+10*b+c
##a=partial(add,c=2,b=1)
##print(a(3))

##from functools import lru_cache
##@lru_cache(maxsize=100)
##def count_vowels(sentence):
##    sentence=sentence.casefold()
##    return sum(sentence.count(vowel) for vowel in "aeiou")
##a=input()
##print(count_vowels(a))

##from functools import total_ordering
##class Order:
##    def __init__(self,value):
##        self.value=value
##    def __lt__(self,other):
##        return self.value <other.value
##    def __eq__(self,other):
##        return self.value == other.value
##print(Order(2)<Order(3))
##print(Order(2)<Order(1))
##print(Order(2)==Order(2))
##print(Order(1)==Order(2))
