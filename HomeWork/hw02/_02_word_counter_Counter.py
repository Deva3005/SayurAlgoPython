# Word Frequency Counter

# Given a paragraph, 
#   count how many times each word occurs.
#   Ignore capitalization 
#   (e.g., "Python" and "python" are the same word).
#   Sort the results by frequency in descending order.
# 
# Input - Python is great. Python is fun. I love Python!
#  
# Output - 
# python: 3
# is: 2
# great: 1
# fun: 1
# i: 1
# love: 1


from collections import Counter

sample_txt='''
Tell tell me is the python python is good 
good language to learn learn learn
who knows knows Im trying to to to get some inputs
before jumping in in in
'''
import string
def word_counter_and_rank(sample_txt:str):

    # Counter from collection module does the counting work and return DICT
    word_count=dict(Counter(sample_txt.strip().lower().split()))

    # Hence the MAX time repeated words are needed, swapping the keys and values
    # key=number_of_times_repeated || value=list_of_repeated_words
    swap_count={}

    # SWAP OPS
    for i,j in word_count.items():
        if j in swap_count:
            swap_count[j]+=[i]
        else:
            swap_count[j]=[]
            swap_count[j]+=[i]
    print()
    # PRINTING ALL repeated word count from reversed order...
    # Output 1
    for i in list(sorted(swap_count.keys(),reverse=True)):
        print(i,"...times Repeated...")
        print(swap_count[i])

    # Modified Output 2
    for i in list(sorted(swap_count.keys(),reverse=True)):
        for j in swap_count[i]:
            print(j.ljust(10,"."),end="")
            print(i,"repeated")

# THE END!!!
word_counter_and_rank(sample_txt=sample_txt)