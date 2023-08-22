import re

text="the quick brown frog jumps over the lazy dog"
pattern=r'\b\w{3,4}\b'
matches=re.findall(pattern,text)
print(matches)