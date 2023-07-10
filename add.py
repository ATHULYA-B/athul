a=[7,8,9,10]
b=[5,6,7,8]
c=[]
i=0
while i<len(a):
  if a[i] in b:
      c.append(a[i])
  i+=1
print(c)
      