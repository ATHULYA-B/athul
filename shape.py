def tri(ch):
    if(ch1==1):
        print("it is an isoceles triangle")
    else:
        print("it is a triangle")
        
def sq(ch):
    if(ch1==1):
        print("it is a square")
    else:
        print("it is a rectangle")
print("enter the number of side shape\n 0 sides\n 2 sides\n 4 sides\n 5 exist")
while True:
    ch=int(input("enter the choice:"))
    if ch==0:
        print("it is a circle")
    if ch==1:
        print("it is a straight line")
    elif ch==3:
        print("is the number of sides equal or not \n 1.yes \n 2.no")
    ch1=int(input("enter the choice:"))
    tri(ch1)
    elif ch==4:
        print("is the number of sides equal or not \n 1.yes \n 2.no")
        ch1=int(input("enter the choice:"))
        sq(ch1)
    elif ch==5:
    print("existing")
    break
    else:
    print("invalid number")
    break
         
                        
    