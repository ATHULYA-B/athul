import re
text="""keep the blue flag \n flying high"""
x=re.sub("\n"," ",text)
print(x)