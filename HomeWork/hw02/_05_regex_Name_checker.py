# Check Valid Name
#     A valid name should:
#        Start with a capital letter.
#        Be followed by lowercase letters.

# Optionally contain a middle initial (like J. or S.).
# Examples:✅ John Smith✅ J. Smith❌ john smith❌ SMITH 

import re

# POSITIVE TEST CASE
sample_txt_1="John Smith"
sample_txt_2="J. Smith"
sample_txt_3="John D. Smith"
sample_txt_4="John Deus Smith"

# * - 0 or many
# + - 1 or many
# ? - 0 or 1

pattern=r"^[A-Z](\.{1}|[a-z]*)\s[A-Z](\.{1}|[a-z]*)(\s[A-Z](\.{1}|[a-z]*))?"
'''
^[A-Z]..............................Startswith Caps [A to Z]
(\.{1}..............................escape character \. {1} exact count
|...................................pipe for 'or'
[a-z]+).............................Followed By lowers [a to z] '+ one or many char'
\s..................................\s means white space
[A-Z]...............................After space startswith Caps [A to Z]
(\.{1}|[a-z]*)
(\s
[A-Z]
(\.{1}|[a-z]*)
)?"
'''

print(re.match(pattern,sample_txt_1))
print(re.match(pattern,sample_txt_2))
print(re.match(pattern,sample_txt_3))
print(re.match(pattern,sample_txt_4))

sample_txt_5="john smith"
sample_txt_6="John s. sailor"
sample_txt_7="JOHN S SAILOR"

print(re.match(pattern,sample_txt_5))
print(re.match(pattern,sample_txt_6))
print(re.match(pattern,sample_txt_7))



