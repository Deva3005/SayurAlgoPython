# Class 1 :: RegEx (a.k.a) Regular Expression


# Home work problems for regular expression:
# :::::::::::::::::::::::::::::::::::::::::::

# 1. Validate a phone number format like 123-456-7890...................................[ok]
# 2. Check if a password has at least one uppercase, one lowercase, and one digit.......[no]
# 3. Extract all hashtags from a social media post......................................[ok]
# 4. Find all occurrences of 'cat' or 'dog' in a text

# Question 00
# Email Validation

# email 'name-example@domain.topLevelDomain

# Name   :: Non Whitespace, AlphaNumber, Allowed Symbols :: \w* --> equivalent to [a-zA-Z0-9], * --> zero or Many
# '@'    :: Symbol at the rate is essential in all email :: @
# domain :: its bunch of words with no whitespace        :: \w*
# '.'    :: Followed by 'period' symbol                  :: \.
# TLD    :: may be like .com or in or .edu or .edu.in    :: .*
# \b     :: set Bounds                                   :: \b

# ANSWER
# [\w\d.-]{5,} :: words,digits
# @
# \w
# \.

import re

text1 = "deva-3005@gmail.com >>> e@e.com [wont come] <<<- check me is a kind of email"
text2 = "wishingGold wish some luck for me deva01@canis.edu.in random words to fill sentences"
text3 = "@sample.com spooky edge case to confuse cause trouble chaos.."


print("\n\nQ0: Validate email\n")
answer = re.findall(r"^[\w.-]{4,}@\w*\.\w{2,}\b",text1)
print(answer)
answer = re.findall(r"[a-zA-Z0-9.-]{4,}@\w*\.\w{2,}\b",text2) 
# ^[a-zA-Z0-9.-]{4,}@\w*\.\w{2,}\b is not working here!!!
print(answer)


# Question 01
# Validate a phone number format like 123-456-7890.

# Breakdown
# Only digits \d{3}-\d{3}-\d{4}

print("\n\nQ1: Validate PhoneNumber as per the Pattern\n")
phone1 = "123-123-1234" # True
answer=re.match(r"\d{3}-\d{3}-\d{4}",phone1)
print(phone1,bool(answer))

phone2 = "12-123-1234" #False
answer=re.match(r"\d{3}-\d{3}-\d{4}",phone2)
print(phone2,bool(answer))

# Question 02 :: 
# Can't DO >>> ?= <<< need help on this

# Check if a password has at least one uppercase, one lowercase, and one digit

# Breakdown
# ^\S   :: starts with non-whitespace characters
# *     :: zero or many
# [A-Z] :: Capital Letters 
# [a-z] :: Small Letters
# [0-9] :: Digits
# {n}   :: Specifying Length

pass1="1234567"
a=re.findall(r".*[a-zA-Z0-9].*",pass1)
print("\n\nQ2: Validate Password atLeast 1Cap, 1Small, 1Num\n")
print(a)

# Question 03 ::
# retrive all the words after Hash #

# Used GROUPING (...)

text="""this is bunch o
f text #angel +91 787878 #bigbuilder 7878 to confuse #boss and add s (999)-909-9890
ome #savior I'll #deva #hashmap embbed some deva3005@gmail.com number #destiny or pa
tterns or passwords to find this is mu LongLiveKing@123
ltiline"""

answer=re.findall(r"#(\w+)",text)
print("\n\nQ3: Find words after hashtag\n")
print(answer)

# Question 04 ::
# Find all cats and dogs in the passage...

# Used GROUPING text* [zero or many]
text="""Lorem catIpsum is simply dummy text of the printing and typesetting 
industrycat. Lorem Ipsum has bcateen the industry's standard dummy
text ever since thedog 1500s, when an unknown printer took a galley 
of type and scrambled it to make a type specimen book.cat It has survived 
not only five centuries, but also the leacatp intcato electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s 
with the releacatse of Letraset sheets containing Lorem Ipsum padogssages, 
and more recentldogy with desktop publishing software like Aldus PageMaker 
includicatng versions of Lorem Ipsumdog"""

answer=re.findall("cat*|dog*",text)
print("\n\nQ4: Find all the cats and dogs\n")
print(answer)