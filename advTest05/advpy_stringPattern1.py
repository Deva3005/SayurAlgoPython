import string

alphabets = string.ascii_lowercase
whereToStop=input("Enter character [which defines where to stop]:: \t")
print()
index1 = alphabets.find(whereToStop)
temp=""
for i in alphabets:
    if i==alphabets[index1+1]:
        break
    temp=temp+i+temp
    print(temp)
