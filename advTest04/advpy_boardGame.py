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

# Matrix Size
matrix=6

def setBoard(n):
    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append("*")
        theBoard.append(temp)
    return theBoard

theBoard=setBoard(matrix) # Set the Matrix :: Board Size
theBoard.append([0,0]) # Temp Space in Board for the piecies got killed
print(theBoard)
    
# POINTS
playerA_pts=0
playerB_pts=0

# 6-Face DIE :: ROLL
def rollDice()->int:
    return random.randrange(0,6) # randrange(start[include],stop[exclude])

# Placing the PIECE and RETURNING CO-ORDINATES
def piecesInBoard(player:str):
    x,y=rollDice(),rollDice()
    theBoard[x][y]=player
    print(player," Roll Roll...")
    printBoard()
    return x,y

# CLEAR THE PIECE before the New position
def clearThePiece(x:int,y:int):
    theBoard [x] [y] ='*'

# PRINT THE BOARD
def printBoard():
    print("+"*10*matrix)
    for i in theBoard:
        print(i)
    print("+"*10*matrix)

# TEMP variables
x,y,x1,y1=0,0,0,0

player1=input("Enter Player 1 Name:")
player2=input("Enter Player 2 Name:")

# MASTER LOOP || HEART OF THE PROGRAM
while True:

    # Debug Lines
    # print("The Last Throws ",x,y,x1,y1)
    # print("+"*20)
    
    cycle+=1

    if playerA_pts==5:
        print(f"{player1} Won the Match")
        break
    if playerB_pts==5:
        print(f"{player2} Won the Match")
        break

    print("Iteration ",cycle)
    clearThePiece(x,y)

    x,y=piecesInBoard(player1)
    if(x==x1 and y==y1):
        print(f"{player1} Score a Point")
        print("+"*10*matrix)
        # print(x,y,x1,y1)
        playerA_pts+=1
        x1,y1=6,1
        theBoard[x1][y1]=player2
        printBoard()

    clearThePiece(x1,y1)

    x1,y1=piecesInBoard(player2)
    
    if(x1==x and y1==y):
        print(f"{player2} Score a Point")
        print("+"*10*matrix)
        # print(x,y,x1,y1)
        playerB_pts+=1
        x,y=6,0
        theBoard[x][y]=player1
        printBoard()
    print()
    print()

print(player1,"........",playerA_pts)
print(player2,"........",playerB_pts)
    
        
        


