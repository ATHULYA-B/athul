import re

s="hari is followed by ansib and arib"
x=re.findall(r'\ba\w*b\b',s)

print(x)
     