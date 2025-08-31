# Sudoku Solver
# Check the Element is not repeated in ROW................[Done]
# Check the Element is not repeated in COLUMN.............[Done]
# Check the Element is not repeated in Subgrid 3x3........[Done]


puzzle1='''
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
'''
puzzle1=puzzle1.split("\n")
testPuzzle=[]
for i in puzzle1:
    if i=="":
        continue
    else:
        try:
            temp_l = list(map(int,i.split(" ")))
            if list(filter(lambda x : x>9,temp_l)):
                print("ERROR :: Validation Issue... some number greater than '9'\n")
                print(temp_l)
                exit(0)
            testPuzzle.append(temp_l) #'''''''If input is Not other than number It will throw Error
        except Exception as e:
            print(e)
            print("SOMETHING WRONG WITH INPUT")
            exit(0)

def CheckSudokuIsSolved(puzzle:list[list[str]])->bool:
    for row in puzzle:
        for element in row:
            pos=row.index(element)#''''''''''''''''''''''''''''getting the column index
            rowPos=puzzle.index(row)#''''''''''''''''''''''''''getting the row index
            # Debugging PRINTS
            # print(element," ----> position",rowPos,pos)#'''''''Element under validation is displayed
            if row.count(element)!=1:#'''''''''''''''''''''''''validating the row contains 1 ENTRY
                print(f"Error in Row {rowPos} itself")
                return False
            for i in range(len(puzzle)):
                if i == rowPos:#'''''''''''''''''''''''''''''''skipping the same row
                    continue
                if element == puzzle[i][pos]:#'''''''''''''''''Itreating to get a match [No Match :: PASSED]
                    print(f"Error in Column check row {i} position {pos}")
                    return False
    return True

def solve3x3grids(puzzle:list[list[str]]):
    print("solving")
    temp=[]#''''''''''''''''''''''''''''''''''''''''''''for gathering grids
    quad=[]#''''''''''''''''''''''''''''''''''''''''''''quad store all the 3x3 grid
    for some in range(3):#''''''''''''''''''''''''''''''Cover all the Rows
        for i in range(len(puzzle)):
            temp.extend(puzzle[i][:3])#'''''''''''''''''Slice and Extending
            for ele in puzzle[i][:3]:#''''''''''''''''''Removing the added things
                puzzle[i].remove(ele)
            if len(temp)==9:#'''''''''''''''''''''''''''If 3x3=9 limits hits append and restore to []
                quad.append(temp)
                temp=[]

    # Debugging PRINTS
    # for i in quad:
    #     print(i)

    for i,x3 in enumerate(quad):#''''''''''''''''''''''''''''''''''''Validate with no duplicates in 3x3 
        if len(x3) != len(set(x3)):#'''''''''''''''''''''''''''''''''Using set to remove duplicates if present
            print("Problem in the quadrant",i)
            return False
    else:
        return True

# When the 2 conditions are PASSED Yes the Puzzle SOLVED !!!
if CheckSudokuIsSolved(testPuzzle) and solve3x3grids(testPuzzle):
    print("Solved")
    print("Thanks for PLAYING!!!")
    print(*puzzle1,sep="\n")
else:
    print("Not Solved Try Again...")
