# Sudoku Solver
# Check the Element is not repeated in ROW................[Done]
# Check the Element is not repeated in COLUMN.............[Done]
# Check the Element is not repeated in Subgrid nxn........[Done]

matrix_size=int(input("Enter the MATRIX size...[example 9 for 9x9=81]...\n"))
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

# puzzle1='''
# 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16
# 05 06 07 08 01 02 03 04 13 14 15 16 09 10 11 12
# 09 10 11 12 13 14 15 16 01 02 03 04 05 06 07 08
# 13 14 15 16 09 10 11 12 05 06 07 08 01 02 03 04

# 02 03 04 01 06 07 08 05 10 11 12 09 14 15 16 13
# 06 07 08 05 02 03 04 01 14 15 16 13 10 11 12 09
# 10 11 12 09 14 15 16 13 02 03 04 01 06 07 08 05
# 14 15 16 13 10 11 12 09 06 07 08 05 02 03 04 01

# 03 04 01 02 07 08 05 06 11 12 09 10 15 16 13 14
# 07 08 05 06 03 04 01 02 15 16 13 14 11 12 09 10
# 11 12 09 10 15 16 13 14 03 04 01 02 07 08 05 06
# 15 16 13 14 11 12 09 10 07 08 05 06 03 04 01 02

# 04 01 02 03 08 05 06 07 12 09 10 11 16 13 14 15
# 08 05 06 07 04 01 02 03 16 13 14 15 12 09 10 11
# 12 09 10 11 16 13 14 15 04 01 02 03 08 05 06 07
# 16 13 14 15 12 09 10 11 08 05 06 07 04 01 02 03
# '''

# puzzle1='''
# 01 02 03 04
# 03 04 01 02
# 02 01 04 03
# 04 03 02 01
# '''

puzzle1=puzzle1.split("\n")
testPuzzle=[]
for j,i in enumerate(puzzle1):
    if i=="":
        continue
    else:
        try:
            temp_l = list(map(int,i.split(" ")))
            if list(filter(lambda x : x>matrix_size,temp_l)) or list(filter(lambda x : x<=0,temp_l)):
                print("row number...",{j-1})
                print(f"ERROR :: Validation Issue... some number greater than '{matrix_size} or less than or equals to {0}'\n")
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
    print(".....")
    print("solving")
    temp=[]#''''''''''''''''''''''''''''''''''''''''''''for gathering grids
    quad=[]#''''''''''''''''''''''''''''''''''''''''''''quad store all the 3x3 grid
    for some in range(int(matrix_size**0.5)):#''''''''''''''''''''''''''''''Cover all the Rows
        for i in range(len(puzzle)):
            temp.extend(puzzle[i][:int(matrix_size**0.5)])#'''''''''''''''''Slice and Extending
            for ele in puzzle[i][:int(matrix_size**0.5)]:#''''''''''''''''''Removing the added things
                puzzle[i].remove(ele)
            if len(temp)==matrix_size:#'''''''''''''''''''''''''''If 3x3=9 limits hits append and restore to []
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
