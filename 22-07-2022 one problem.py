'''
1) using functools write a program on partialmethod, url_cache and total_ordering '''




##from functools import partial

##def fun(a,b):
##    return a*b
##obj=partial(fun,b=2)
##result=obj(10)
##
##print(result)


##from functools import lru_cache
##
##@lru_cache(maxsize = None)
##def fac(n):
##    if n<=0:
##        return 1
##    return n*fac(n-1)
##print([fac(n) for n in range(7)])
##print(fac.cache_info())


##from functools import total_ordering
##  
##@total_ordering
##class N:
##    def __init__(self, value):
##        self.value = value
##    def __eq__(self, other):
##        return self.value == other.value
##  
##    # Reverse the function of 
##    # '<' operator and accordingly
##    # other rich comparison operators
##    # due to total_ordering decorator
##    def __lt__(self, other):
##        return self.value > other.value
##  
##  
##print('6 > 2 :', N(6)>N(2))
##print('3 < 1 :', N(3)<N(1))
##print('2 <= 7 :', N(2)<= N(7))
##print('9 >= 10 :', N(9)>= N(10))
##print('5 == 5 :', N(5)== N(5))



