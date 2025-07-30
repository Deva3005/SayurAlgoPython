'''
Me and The Devil
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

def resetBoard():
    for i in range(6):
        temp=[]
        for j in range(6):
            temp.append("0")
        theBoard.append(temp)
    return theBoard

theBoard=resetBoard()
theBoard.append([0,0])
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
    theBoard [x] [y] ='0'

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
    print("Iteration",cycle)
    cycle+=1
    if playerA_pts==5:
        print("I Won the Match")
        break
    if playerB_pts==5:
        print("Devil Won the Match")
        break
    
    clearThePiece(x,y)
    x,y=piecesInBoard("ME")
    print("Me::::::",x,y)

    if(x==x1 and y==y1):
        print("I Score a Point")
        printBoard()
        print(x,y,x1,y1)
        playerA_pts+=1
        x1,y1=6,1
    clearThePiece(x1,y1)
    x1,y1=piecesInBoard("The Devil")
    print("Devil:::",x1,y1)
    if(x1==x and y1==y):
        print("Devil score a Point")
        printBoard()
        print(x,y,x1,y1)
        playerB_pts+=1
        x,y=6,0
    printBoard()
    print("...resetting...")

print("Me......",playerA_pts)
print("Devil...",playerB_pts)
    
        
        


