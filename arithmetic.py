def sum():
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print(a+b)
def sub():
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print(a-b)
while True:
    ch=int(input("enter the choice"))
    if ch==1:
        sum()
    elif ch==2:
        sub()
    elif ch==3:
        print("invalid choice")
        break