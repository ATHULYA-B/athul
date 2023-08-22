def create(list):
    element=(input("enter the elements"))
    for element in element:
        list.append(element)
    return list

def insert(list,element):
    list.append(element)
    return list

def delete(list,element):
    index=list.index(element)
    del list[index] 
    return list

def sort(list):
    new_list=list[:]
    new_list.sort()
    return new_list

print("enter your choices/n 1.create/n 2.insert/n 3.delete/n 4.sort/n 5.Exit")
new=[]
while True:
    ch=int(input("enter the choice:"))
    
    if ch==1:
      print(create(new))  
    elif ch==2:
        n=input("enter the element to add in the list")
        print(insert(new,n)) 
    elif ch==3:
        a=input("enter the element you want to delete")
        print(delete(new,a))
    elif ch==4:
        print(sort(new))
    elif ch==5:
        print("Exiting")
        break
    else:
        print("invalid number") 
        break
                     
    
    