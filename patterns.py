n=int(input("enter limit:"))
print("*")
for i in range(1,n+1):
    print("*",end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):    
        print(j,end="")
    print("*",end="")
    print()
            
for i in range(n-1,0,-1):
    print("*",end="")
    for j in range(1,i+1):
            print(j,end="")
    for j in range(i-1,0,-1):
            print(j,end="")
    print("*",end="")
    print()
print("*")           