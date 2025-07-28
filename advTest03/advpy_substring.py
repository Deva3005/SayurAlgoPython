'''
Read a passage from a file. 
(If you don't know how to handle files in Python, you can hardcode a long passage)

?? Problem Statement ??

Count the number of times the 
word 'the' followed by another 'the' without the letter 'a' in between the two 'the' words.

:: Example :: 

The king went to----------------no  'a' in substring [1]
the forest with-----------------no  'a' in substring [2]
the wife and a servernt.--------yes 'a' in substring
The king shot a deer.-----------yes 'a' in substring
The king went to----------------no  'a' in substring [3]
the forest again----------------yes 'a' in substring
the next day.-------------------yes 'a' in substring
The end.------------------------no  'a' in substring [4] if last one is added :)

+++ Output +++

Answer is 4 
(The king, the forest, The King,
[the next])
 + doubt??? focus loss in explaination]).

'''

# ACT I
# Converting file to proper string :: Removed NewLines and Tabs
def formatFile(filePath:str)->str:
    with open(filePath,"r") as inputFile:
        paragraph = inputFile.read().replace("\n"," ").replace("/t"," ")
        return paragraph

# ACT II
# Logic To find the 'a' in the Substring betweens 'THE'.ignore case
# We Need index | below function will take care on getting those index      
def gettingIndexes(paragraph:str)->tuple:
    refWordList=[]
    indexList=[]
    wordList=paragraph.split(" ")
    for i in range(len(wordList)):
        if wordList[i].lower() == "the":
            indexList.append(i)
            refWordList.append(wordList[i]+" "+wordList[i+1])
    return indexList,refWordList

# ACT III
# We Reached the Climax, when the Substring doesn't contains 'a' yeaaaah!!!
# We append those in things in answer list and return to console
def gettingAnswer(paragraph:str,indexList:list,refWordList:list)->list:  
    answer=[]
    wordList = paragraph.split()
    for i in range(len(indexList)):
        if(i==len(indexList)-1):
            continue
            temp=" ".join(wordList[indexList[i]])
        else:
            temp=" ".join(wordList[indexList[i]:indexList[i+1]])

        ### TIME TO DEBUG & VALIDATE ### Caution use Small test Data!!!
        # print(temp.replace("a","A"*5)) 

        if " a " not in temp:
            if "a" not in temp:
                answer.append(refWordList[i])
    return answer

# READ ONLY METHOD TO TEST SOME FILES
def runAdvpy3(filePath:str):

    # It's ACTION time
    # When FUNCTIONS Calls!!!
    # Drop the Absoulte path of the file Here as an required need input!!!
    paragraph=formatFile(filePath)
    paragraph=formatFile(filePath)
    requiredData=gettingIndexes(paragraph)

    # THE REAL ANSWER #
    # FINAL PLAY #
    answer=gettingAnswer(paragraph,refWordList=requiredData[1],indexList=requiredData[0])
    print(f"The Number of Words which met the criteria are:: {len(answer)}\n+++Result+++")
    print(*answer,sep=", ")


# THE END #
runAdvpy3("./SayurAlgoPython/advTest03/advpy_test03.txt")