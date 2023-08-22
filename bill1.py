Dict={'t-shirt':350,'shirt':450,'jeans':400,'pants':150}
i=1
c={}
sum=0
while i<4:
    a=input("enter the item:")
    if a.lower()=="quit":
        break
    else:
     c.update({a.Dict[a]})
     sum+=Dict[a]
    i=i+1
print(c)
print("total price:",sum)