"""
Problem:
Given a list and a target, find all pairs that sum to the target.
Example: [2, 4, 3, 7, 5, -1] and target 6 → (2,4), (3,3), (7,-1).
"""

arr=[2,4,3,7,5,-1]
num=6

def find_the_pairs(array:list[int],number:int):
    ans=[]
    for i in arr:#............................Iterrating over the Array
        # CORE OF THE PROGRAM IS HERE
        for j in arr[arr.index(i):]:#.........[*] Creating Subset from starting with the element
            if i+j == num:#...................If sum met the Number
                ans.append((i,j))#............Appending to Answer array
    if len(ans)==0:#..........................If No Pairs Found
        print("NO MATCH FOUND!!!")#...........LET THEM KNOW!!!
    else:#....................................else
        print(ans)#...........................PRINTING THE ANSWER [Easy!!!]

find_the_pairs(array=arr,number=6)