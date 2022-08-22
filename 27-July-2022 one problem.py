'''
Let's dive into decorators! You are given N mobile numbers.
Sort them in ascending order then print them in the standard format shown below:
+91 xxxxx xxxxx
The given mobile numbers may have +91,91 or 0 written before the actual 10 digit number.
Alternatively, there may not be any prefix at all.


Input Format

The first line of input contains an integer N, the number of mobile phone numbers.
N lines follow each containing a mobile number.

Output Format

Print N mobile numbers on separate lines in the required format

Sample Input:
3
07895462130
919875641230
9195969878


Sample Output:
+91 78954 62130
+91 91959 69878
+91 98756 41230

Hint:
To solve the above question, make a list of the mobile numbers and pass
it to a function that sorts the array in ascending order.
Make a decorator that standardizes the mobile numbers and apply it to the function.
'''
##def phone(number):
##    def mphone():
##        number=int(input("enter a phone number:"))
##        b=str(number)
##        if len(b)==10:
##            print("+91",b)
##        elif len(b)==12 and b[0]=='9' and b[1]=='1':
##            print("+",b[0:2],b[2:])
##        elif len(b)==11 and b[0]=="0":
##            del(b[0])
##            print("+91",b)
##    return mphone()
##@phone
##def phonenumber():
##    pass
##phonenumber

    
