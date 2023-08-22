class Calc():
    def __init__(self,n,m):
        self.num1=n
        self.num2=m
    def Add(self):
        self.sum=self.num1+self.num2
        return self.sum
Add1=Calc(10,20)
print(Add1.Add())
Add2=Calc(20,15)
print(Add2.Add())