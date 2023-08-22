import re

def check_string(input_string):
    pattern="^[A-Za-z_]+$"
    if re.match(pattern,input_string):
        return "String contains only uppercase and lowercase letters and underscores"
    else:
        return "String contains characters other than uppercase and lowecase letters and underscores"
    
test_string="Hello_World"
result=check_string(test_string)
print(result)






















