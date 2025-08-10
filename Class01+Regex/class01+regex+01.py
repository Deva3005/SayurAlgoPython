# Regex -> Regular Expression
# AUG 10 :: SUNDAY :: 2025

r'''

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

import re

print(*dir(re),sep="\n")

# Script is under MAINTENANCE 
# Not ready for DISPLAY!!!