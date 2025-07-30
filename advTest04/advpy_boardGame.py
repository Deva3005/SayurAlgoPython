'''
You have 6 x 6 game board where each cell is shown as a *

This is a two player dice game. 

The die has numbers 1 to 6.

Each player rolls the dice twice. 
First roll is row number, 
second roll is col number.

After the player rolls the dice, in the (row,col) enter the player's initial. 
If the player A rolls the dice and if player B already has their initial in the same row,col
add a point to A and change the initial to A. 

Player who gets 5 points first wins the game.

Me and The FOE
Walking side by side...
'''
# To Generate RANDOM numbers between 0 and 5 [6]
import random

# TO CLEAR THE CONSOLE SCREEN
import os

# TO STOP THE THREAD FOR TIME BEING...FOR HYPING WINNER!
import time

# THE GAME BOARD
theBoard=[]

# CYCLES
cycle=1

def setBoard(n):
    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append("*")
        theBoard.append(temp)
    return theBoard

theBoard=setBoard(6) # Set the Matrix :: Board Size
theBoard.append([0,0]) # Temp Space in Board for the piecies got killed
print(theBoard)
    
# POINTS
playerA_pts=0
playerB_pts=0

# ROLL
def rollDice()->int:
    return random.randrange(0,6) # randrange(start[include],stop[exclude])

# Placing the PIECE and RETURNING CO-ORDINATES
def piecesInBoard(player:str):
    x,y=rollDice(),rollDice()
    # print(x,y)
    theBoard[x][y]=player
    return x,y

# CLEAR THE PIECE before the New position
def clearThePiece(x:int,y:int):
    theBoard [x] [y] ='*'

# PRINT THE BOARD
def printBoard():
    print("+"*10)
    for i in theBoard:
        print(i)
    print("+"*10)

# TEMP variables
x,y,x1,y1=0,0,0,0

# MASTER LOOP || HEART OF THE PROGRAM
while True:
    print("The Last Throws ",x,y,x1,y1)
    print("+"*20)
    
    cycle+=1
    if playerA_pts==5:
        print("I Won the Match")
        break
    if playerB_pts==5:
        print("The FOE Won the Match")
        break
    print("Iteration ",cycle)
    clearThePiece(x,y)
    x,y=piecesInBoard("ME")
    print("Me::::::::",x,y)

    if(x==x1 and y==y1):
        print("I Score a Point")
        printBoard()
        print(x,y,x1,y1)
        playerA_pts+=1
        x1,y1=6,1
    clearThePiece(x1,y1)
    x1,y1=piecesInBoard("The FOE")
    print("The FOE:::",x1,y1)
    if(x1==x and y1==y):
        print("The FOE score a Point")
        printBoard()
        print(x,y,x1,y1)
        playerB_pts+=1
        x,y=6,0
    printBoard()
    print("...resetting...")

print("Me........",playerA_pts)
print("The FOE...",playerB_pts)
    
        
        


