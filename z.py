import re
text="zebra starts with the letter z"
pattern=r'\b\w*z\w*\b'
matches=re.findall(pattern,text,re.IGNORECASE)
print(matches)