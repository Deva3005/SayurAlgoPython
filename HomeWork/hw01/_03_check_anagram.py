def check_anagram(letter1:str,letter2:str)->bool:
    # print()
    if(len(letter1)!=len(letter2)):
        # print(letter1,"...",letter2)
        # print("IS NOT AN ANAGRAM...")
        return False
        
    for i in letter1:
        if letter1.count(i)==letter2.count(i):
            pass
        else:
            # print(letter1,"...",letter2)
            # print("IS NOT AN ANAGRAM...")
            return False
    else:
        # print(letter1,"...",letter2)
        # print("It is AN ANAGRAM!!!")
        return True
    
# check_anagram("dev1","aved2")
# check_anagram("listen","silent")
# check_anagram("devil","lived")
# check_anagram("dog","god")
# check_anagram("eel","lee")