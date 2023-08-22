fruits=['Apple','Banana','Pear','Apricoats','Orange']
def alpha(s,k):
    if s[0]=='A':
        k.append(s)
    return s
result=map(alpha,fruits)
print(list(result))