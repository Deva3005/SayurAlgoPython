# HIGHER ORDER FUNCTION MRF(MAP, REDUCE, FILTER)
# SYNTAX: ```keyword(function,iterables)```

# LAMBDA
# SYNTAX: ```keyword [`arguments`]:[`expression|return things auto`]```
# lambda: x : x+10 (10) -> 20

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Filter Even Numbers
# Use filter with a lambda to extract only even numbers from a list.
# Example: [1,2,3,4,5,6] → [2,4,6]

test_array_1=[1,2,3,4,5,6]
answer=list(filter(lambda x:x%2==0,test_array_1))
print("\n#_01...Filter Even Numbers...")
print(answer)

# Sort Tuples by Second Value
# You are given: [(1, 5), 2, 1),(3, 7)]
#...................2.....1.......3...Ascending...
# Sort by the second element using a lambda.Expected: [(2, 1), (1, 5), (3, 7)]

test_array_2=[(1, 5), (2, 1), (3, 7)]
print("\n#_02...Sort ascending list[tuple[int,int]]...")
print(sorted(test_array_2,key=lambda x:x[1]))

# Add Two Numbers
# Write a lambda that takes two numbers and adds them.
# Example: (5, 7) → 12
# REDUCE

from functools import reduce
test_array_3=(5,7,3)
print("\n#_03...Use Reduce method to sum numbers...")
print(reduce(lambda x,y:x+y,test_array_3))

# Maximum of Two Numbers
# Write a lambda to return the greater of two numbers.

test_array_4=[1,2,3,100]
print("\n#_04...Max of Two or MORE...")
print("Test Array",test_array_4)
print(reduce(max,test_array_4)) #OR 
print(reduce(lambda x,y:x if x>y else y,test_array_4))

# Filter Names Starting with ‘A’
# From ["Alice", "Bob", "Anu", "Mohan"], 
# use filter with lambda to find names starting with "A".

test_array_5=["Alice", "Bob", "Anu", "Mohan","Alucard"]
print("\n#_05filter with lambda to find names starting with 'A'")
print(list(filter(lambda x:x.startswith("A"),test_array_5)))

# Square of Numbers
# Use map with a lambda to get the square of all numbers in a list.
# Example: [1, 2, 3, 4] → [1, 4, 9, 16]

test_array_6=list(range(1,5))
print("\n#_06...Map with SQUARE_Numbers...")
print(list(map(lambda x:x**2,test_array_6)))

# Word Lengths
# Given ["apple", "banana", "cherry"], 
# use map with lambda to return their lengths.Expected: [5, 6, 6]

test_array_7=["apple", "banana", "cherry"]
print("\n#_07...Map with Length of the word...")
print(list(map(lambda x:len(x),test_array_7)))

# Multiply All Numbers
# Use reduce with lambda to 
# multiply all numbers in a list.Example: [2, 3, 4] → 24

test_array_8=[2, 3, 4]
print("\n#_08...Use Reduce method to Multiply numbers...")
print(reduce(lambda x,y:x*y,test_array_8))

# Convert List of Integers to Strings
# Given [1, 2, 3, 4], use map with lambda to get ["1", "2", "3", "4"].

test_array_9=list(range(5))
print("\n#_09...Map Integer to String...")
print(list(map(str,test_array_9))) # OR
print(list(map(lambda x:str(x),test_array_9)))

# Custom Sorting of Strings
# Given ["apple", "banana", "kiwi", "mango"], 
# sort by string length using lambda.Expected: ["kiwi", "mango", "apple", "banana"]

test_array_10=["apple", "banana", "kiwi","kawa", "mango"]
print("\n#_10...Sort based on length of the word...")
print(sorted(test_array_10,key=lambda x:len(x)))
print(sorted(test_array_10,key=len))


