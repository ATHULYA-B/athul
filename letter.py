import re
text="this is a simple text with some words containing the word zebra"
pattern=r'\b\w*z\w*\b'
matches=re.findall(pattern,text,re.IGNORECASE)
print(matches)