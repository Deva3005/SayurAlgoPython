# CODE NAME: BEST DENOMINATION EVER using MODULO
# 


# NOTE :: Comments may not be pleasing upto your MARK
# No Class No Methods
# Just Logic, Just Fun in cracking...

# Getting Denomination from USER Inputs
denomination = list(map(int,input("Enter the Available Denomination....(seperate by comma ',')...\n").split(",")))

# Getting Non Negative Balance input from USER
balance = int(input("Enter the Balance :: [No Negative Number]\t"))

# Answer will be in Dictionary [Map] Datatype "Denomination":"count"
answer={}

# EDGE CASE >>> If number is less than or equals 0 [ -lt 0 ] [CLIFF AHEAD CAREFUL BCOZ of Edge...] 
if(balance<=0):
    print("Don't Blame I Warned You!, Bye [I'm Only Human After All...RagNBone]") # Not in Serious TONE
    exit(0)

# I Need this Temp Variable I'll keep the balance variable and show it in the end...,
temp = balance

# While Loop
# BRUTE FORCE PRIMATE INTELLIFORCE [ACTIVATE]
while (temp != 0): # CONDITION Until temp get ZERO
    
    for i in reversed(denomination):
        if temp==0:
            break
        if i==1:
            continue
        if temp%i==0:
            answer.setdefault(i,0)
            answer[i]=temp//i
            temp=0
    if temp>=max(denomination): # HERE it Choose the Best Denomination // Forget SORTING it takes the MAX()
        answer.setdefault(max(denomination),0)
        answer[max(denomination)] = temp//max(denomination) # INCREAMENTING || Serious FIX Added here
        temp%=max(denomination) # DONE !!! <- here... ReArranged 
    else:
        denomination.remove(max(denomination)) #

# CONSOLE :: OUTPUT :: PART
# CURATED PRINT STATEMENTS...
print()
print("The BEST Denomination ever")
for i in answer:
    print(i,"......x",answer[i]," = ",i*answer[i])

print("TOTAL\t\t",balance)