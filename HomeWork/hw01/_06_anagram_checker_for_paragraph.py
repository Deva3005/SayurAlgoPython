import _03_check_anagram as ca

s="Python listen silent god dog deva aved rat tar art is great. Python is fun. I love Python!"

def anagram_checker_in_paragraph(sample_txt:str)->list[list]:
    list_from_txt=s.strip().split(" ")
    answer=[]
    for i in list_from_txt:
        list_from_txt.remove(i)
        temp=[]
        temp.append(i)
        for j in list_from_txt+[" "]:
            if ca.check_anagram(i,j):
                temp.append(j)
                list_from_txt.remove(j)
        if len(temp)>1:
            answer.append(temp)
    return answer


print(anagram_checker_in_paragraph(s))