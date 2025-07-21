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

Missed Point compare the 3 integers and find which take less steps to reach 1
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

counter=0
def recurNumber(n):
    if (n<1 or type(n) != int):
        print("DO PROVIDE PROPER INPUTS (^_^) Bye!")
        exit(0)
    global counter
    if n==1:
        print(n)
        counter+=1
        temp = counter
        counter=0
        return temp
    else:
        if(n%2==0):
            print(n,end=",")
            counter+=1
            return recurNumber(n//2)
        else:
            print(n,end=",")
            counter+=1
            return recurNumber((3*n)+1)
        
a,b=map(int,input("Enter 2 numbers [non-negative, RealNumbers] with space\n").split())
x,y=map(recurNumber,[a,b])

if x>y:
    print(f"Number {b} takes {y} to reach 1")
else:
    print(f"Number {a} takes {x} to reach 1")
