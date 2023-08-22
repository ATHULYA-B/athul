def prime(num):
    if num<=1:
      print("not prime")
      for i in range(2,num):
        if num%i==0:
            print("not prime")
print("prime")
n=int(input("enter a number"))
print(n)