# Extract Dates
# From a text, extract all dates in the format dd-mm-yyyy or dd/mm/yyyy.
# Example input:
#   My birthday is on 12-05-2000, and my brother's is 01/01/1995.
# Expected output:
#   ['12-05-2000', '01/01/1995']

import re

sample_txt="My birthday is on 12-05-2000, and my brother's is 01/01/1995."

answer=re.findall(r"(\d{2}[\-\/]\d{2}[\-\/]\d{4})",sample_txt)
print(answer)