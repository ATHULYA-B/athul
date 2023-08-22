def fact(n ):
    if n==0:
        return(1)
    else:
        n=n*fact(n-1)
        return n
b=int(input("enter the number:"))
print(fact(b))        