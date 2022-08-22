## TryExceptElse
###===============================

##x=150
##y=0
##try:
##    z=x/y
##    print(z)
##    print("inside try")
##
##except ZeroDivisionError:
##    print("Division by Zero not allowed pleas try onther number")
##else:
##    print("inside else")

## Except
###=============================

##x=10
##y=5
##try:
##    z=x/y
##    print(z)
##except:
##    print("Exception handling")

### AssertStatement
###============================

##a=20
##assert a <= 10, 'vadeppa invalid'
##print('no error')

### CustomeException
#==========================

##class BalanceException(Exception):
##    def __init__(self,x):
##        self.msg=x
##def checkbalance():
##    money=20000
##    withdraw=19000
##    try:
##        balance=money-withdraw
##        if (balance <= 500):
##            raise BalanceException('insufficient balance')
##        print(balance)
##    except BalanceException as b:
##        print(b)
##checkbalance()

## ExceptMultiple
#=============================

##x=10
##y=15
##try:
##    z=x/l
##    print(z)
##except (NameError , ZeroDivisionError)as ex:
##    print(ex)
##print('Rest of the code')

## TryExcept
#===============================

##x=10
##y=0
##try:
##    z=x/y
##    print(z)
##except ZeroDivisionError:
##    print("zerodivision error is not allowed")
##print("Rest of the code")

## TryExceptElseFinally
#==================================

##x=12
##y=0
##try:
##    z=x/y
##    print(z)
##    print('inside try')
##except ZeroDivisionError:
##    print("Division by zero not allowed")
##finally:
##    print('inside finally')
##print("Rest of code")

## ExceptMultiple
#====================================

##x=0
##y=10
##try:
##    z=y/x
##    print(z)
##    print("inside try")
##except (ZeroDivisionError) as Z:
##    print(Z)
##except NameError as N:
##    print(N)
##print("Rest of the code")

## ExceptObj
#=====================================

##x=10
##y=0
##try:
##    z=x/y
##    print(z)
##    print("inside try")
##except ZeroDivisionError as Z:
##    print(Z)
##print("Rst of the code")
