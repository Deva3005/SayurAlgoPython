'''
HW - You have 6 x 6 game board where each cell is shown as a *
This is a two player dice game. The die has numbers 1 to 6.
Each player rolls the dice twice. First roll is row number, second roll is col number.
After the player rolls the dice, in the (row,col) enter the player's initial. 
If the player  A rolls the dice and  if  player B already has their initial in the same row,col
add a point to A and change the initial to A. 

Player who gets 5 points first wins the game.

'''


#NIMPORTING RANDOM LIBRARY FOR GENERATING NUMBER BETWEEN 0 AND 6
import random

# POINTS
play_A=0
play_B=0

# POSITIONS
x,y,x1,y1=0,0,0,0

print("Game Start...")
totalAttempts=0

# HEART OF THE BOARD GAME LOGICS
while True:
    totalAttempts+=1
    if(play_A==5): # TO STOP LOOP
        print("A is the Winner !!!")
        break
    if(play_B==5): # TO STOP LOOP
        print("B is the Winner !!!")
        break
    for i in "A","B":  # It is REQUIRED TO CONTINUE GAME UNTIL EITHER ONE OF THEM --> You know what i'm going to say
        if i == "A": # A TURN
            x,y=random.randrange(0,6), random.randrange(0,6)
            if(x==x1 and y==y1):
                print("Previous B's Value",x1,y1)
                print("A Rolls ",x,y)
                print("+"*10,"A 1+ Point...")
                play_A+=1 # Incrementing A's point
                x1,y1=0,0 # Reset B the Position
        else: # B TURN
            x1,y1=random.randrange(0,6), random.randrange(0,6)
            if(x1==x and y1==y):
                print("Previous A's Value",x,y)
                print("B Rolls ",x1,y1)
                print("+"*10,"B 1+ Point...")
                play_B+=1 # Incrementing B's point
                x,y=0,0 # Reset A the Position

# CONCLUSION...
print("Fair Trail: on over total attempts",totalAttempts)
print("Player Score A",play_A)
print("Player Score B",play_B)