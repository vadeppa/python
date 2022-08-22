##Today's task for you guys will be to develop your first-ever Python game i.e., "Snake Water Gun."
##
##Most of you must already be familiar with the game. Still, I will provide you with a brief description.
##
##This is a two-player game where each player chooses one object.  As we know, there are three objects, snake, water, and gun. So, the result will be 
##
##Snake vs. Water: Snake drinks the water hence wins.
##Water vs. Gun: The gun will drown in water, hence a point for water
##Gun vs. Snake: Gun will kill the snake and win.
##In situations where both players choose the same object, the result will be a draw.
##Now moving on to instructions:
##You have to use a random choice function that we studied in tutorial #38, to select between, snake, water, and gun.
##You do not have to use a print statement in case of the above function.
##Then you have to give input from your side.
##After getting ten consecutive inputs, the computer will show the result based on each iteration.
##You have to use loops(while loop is preferred).
## 

##import random
##while(True):
##    player1 = input("Select snake, water, or gun :").lower()
##    player2 = random.choice(["snake", "water", "gun"]).lower()
##    print("Player 2 selected: ", player2)
##    if player1 == "water" and player2 == "snake":
##        print("computer Won")
##    elif player1 == "gun" and player2 == "water":
##        print("computer Won")
##    elif player1 == "snake" and player2 == "gun":
##        print("computer Won")
##    elif player1 == player2:
##        print("Tie")
##    else:
##        print("user Won")
##    continue

