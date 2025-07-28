'''
Its is a GAME
Welcome to {{ BRAMAYUGA }} Board GAME
TWO PEOPLE ENTER ONE LEAVE ALIVE or ENSLAVED IN THIS MANSION FOREVER :)
That is FATE &
That is KODUMAN POTTI for you!!!
'''
import random

# TO CLEAR THE CONSOLE SCREEN
import os
# TO STOP THE THREAD FOR TIME BEING...FOR HYPING WINNER!
import time

# THE GAME BOARD
theBoard=[]
for i in range(6):
    temp=[]
    for j in range(6):
        temp.append("0")
    theBoard.append(temp)
    
# POINTS
playerA_pts=0
playerB_pts=0

def rollDice()->int:
    return random.randrange(0,6) # randrange(start[include],stop[exclude])

def displayBoard():
    for i in range(len(theBoard)):
        for j in range(len(theBoard)): # ROW
            print(theBoard[i][j],end=" ") # COLUMN
        print()

def piecesInBoard(player:str):
    theBoard[rollDice()][rollDice()]=player
    print(theBoard)

piecesInBoard("A")