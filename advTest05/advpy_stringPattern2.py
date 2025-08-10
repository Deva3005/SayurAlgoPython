'''
Another HomeWork 2:

Write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab 
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint - 
there are many simple answers. you can try with slice function
'''


# print(s2[s2.index(s1[0]):]+s2[:s2.index(s1[0])])

def checkString(s1:str,s2:str)->bool:
    # s1=s1.split(" ")
    # s2=s2.split(" ")
    print(s2[s2.index(s1[0]):]+s2[:s2.index(s1[0])])
    if s1 == s2[s2.index(s1[0]):]+s2[:s2.index(s1[0])]:
        print(True," Same Sequence Rotated")
        return True
    else:
        print(False," Not a Same Sequence")
        return False
    

# Test case 1:
print()
print('checkString("ABCD","CDAB")')
checkString("ABCD","CDAB")
print()
# Test case 2:
print('checkString("ABCD","CDBA")')
checkString("ABCD","CDBA")
print()
# Test case 3:
print('checkString("123456","456123")')
checkString("123456","456123")
print()
# Test case 4:
print('checkString("123456","412356")')
checkString("123456","412356")
print()


checkString("Hello Python ","Python Hello ") # Error:: Question Out Of Bound 
