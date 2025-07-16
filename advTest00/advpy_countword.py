'''
Count how frequent word got repeated in Textfile

1. Open File [File Ops]
2. Choose Proper Datatype
3. Print the counts

Extra:
1. Count Words + Letters ✅
2. get the nth high frequent word

'''

with open(r"c:\Users\Thiruppathi\Documents\deva\advTest00\index.html","r") as textFile:
    textfile = textFile.read()
    print(textfile)
    wordDictionary=dict()

    # Word Count
    for i in textfile.split():
        if i in wordDictionary:
            wordDictionary[i]+=1
        else:
            wordDictionary[i]=1
    
    letterDictionary=dict()
    #letter Count
    for i in textfile:
        if i in letterDictionary:
            letterDictionary[i]+=1
        else:
            letterDictionary[i]=1

print(wordDictionary)
print(letterDictionary)

#Frequency
freq=sorted(set(wordDictionary.values()), reverse=True)
# print(freq)
#print nth high frequent word
wordDict_1 = dict()
for i in freq:
    for j in wordDictionary:
        if wordDictionary[j] == i:
            wordDict_1.setdefault(i, []).append(j)
# print(wordDict_1)

# 2nd high frequent word
print(wordDict_1[freq[1]])