string=["hello"]
count={}
index=0
length=len(string)    
while index<length:
    char=string[index]
    if char in count:
        count[char]+=1
    else:
        count[char]=1
        index+=1
return count