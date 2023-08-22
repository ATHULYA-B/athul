import re

s="1 12 123 1567 14321"
x=re.findall("\d{3,}",s)


print(x)