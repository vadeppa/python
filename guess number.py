
##Number Guessing: Python beginners can start with number guessing projects that can be exciting and offer a good learning experience.
##The mini-game can include random numbers between 1 to 10, 1 to 100, etc. followed by a hint so that users can guess the right numbers.
##A simple game will include the major forms of numbers including divisible, multiples, and other combinations. 
##
 
import random
import math
n1 = int(input("Enter Lower bound:- "))
n2 = int(input("Enter Upper bound:- "))
x = random.randint(n1, n2)
print("\n\tYou've only ",
	round(math.log(n2 - n1 + 1, 2)),
	" chances to guess the integer!\n")
if x%5==0:
        print("the guess number is divisible with 5")
if x%3==0:
        print("the  guess number is divisible with 3")
if x%2==0:
        print("it is even number")
if x%2!=0:
        print("it is odd number")
count = 0
while count < math.log(n2-n1+ 1, 2):
	count += 1
	guess = int(input("Guess a number:- "))
	if x == guess:
		print("Congratulations you did it in ",count, " try")
		#break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")
if count >= math.log(n2 - n1+ 1, 2):
	print("\nThe number is " , x)
	print("\tBetter Luck Next time!")



