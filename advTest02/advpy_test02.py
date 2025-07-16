'''
if the number is odd : return 3n+1
if the number is even: return n/2
repeat the process until the number is 1

Example:
    
    n=8
    output:
    8,4,2,1

    n=9
    output
    9,28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1

Approach 
1. Raw Logic
2. Recursion 
'''

# Brute Force
print("\nRaw Logic\n")

n = 8
while(True):
    if(n!=1):
        print(n,end=",")
        if(n%2==0):
            n=n//2
        else:
            n=(3*n)+1
    else:
        print(n)
        break

# Recursion
print("\nRecursion Technique\n")

def recurNumber(n):
    if n==1:
        print(n)
        return 1
    else:
        if(n%2==0):
            print(n,end=",")
            return recurNumber(n//2)
        else:
            print(n,end=",")
            return recurNumber((3*n)+1)
        
recurNumber(8)
recurNumber(9)