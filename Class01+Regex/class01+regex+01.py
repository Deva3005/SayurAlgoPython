# Regex -> Regular Expression
# AUG 10 :: SUNDAY :: 2025

r'''
reference: JAI BAHUBALI !!!
https://www.w3schools.com/python/python_regex.asp
https://regex101.com/
https://regexone.com/references/python

^        :: Starts with
$        :: Ends with
+        :: One or Many
[a-z]    :: anything between a and z
[A-Z]    :: anything between A and Z
[0-9]    :: anything between 0 and 9
\w       :: words
\d       :: digits
\b       :: breakspace [Whitespace]
\.       :: escape slash >>> period
*        :: a*  means repeated aaaa's


re Methods

findall("pattern","text")
match("pattern","text")
search("pattern","text")

'''

'''
Home work problems for regular expression:

1. Validate a phone number format like 123-456-7890.
2. Check if a password has at least one uppercase, one lowercase, and one digit.
3. Extract all hashtags from a social media post.
4. Find all occurrences of 'cat' or 'dog' in a text

'''

import re

print(*dir(re),sep="\n")

# Script is under MAINTENANCE 
# Not ready for DISPLAY!!!