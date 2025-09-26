# Find Anagrams in a List

# Given a list of words, group together words that are anagrams.

# Example input:
# ["listen", "silent", "enlist", "rat", "tar", "art"]
# Expected output:
# [['listen', 'silent', 'enlist'], ['rat', 'tar', 'art']]


from _00_check_anagram import check_anagram

sample1="Python listen silent god dog deva aved rat tar art is great. Python is fun. I love Python!"

def anagram_checker_in_paragraph(sample_txt:str)->list[list]:
    list_from_txt=sample_txt.strip().lower().split(" ")
    answer=[]
    for i in list_from_txt:
        list_from_txt.remove(i)
        temp=[]
        temp.append(i)
        for j in list_from_txt+[" "]:
            if check_anagram(i,j):
                temp.append(j)
                list_from_txt.remove(j)
        if len(temp)>1:
            answer.append(temp)
    return answer


# print(anagram_checker_in_paragraph(sample_txt=sample1))

sample2=["listen", "silent", "enlist", "rat", "tar", "art"]
print(anagram_checker_in_paragraph(sample_txt=" ".join(sample2)))