# print(s2[s2.index(s1[0]):]+s2[:s2.index(s1[0])])

def checkString(s1:str,s2:str)->bool:
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
