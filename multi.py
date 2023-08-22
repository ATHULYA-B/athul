class Calc():
    def __init__(self,n,m):
        self.num1=n
        self.num2=m
    def Mul(self):
        self.sum=self.num1*self.num2
        return self.sum
Mul1=Calc(10,20)
print(Mul1.Mul())
Mul2=Calc(20,15)
print(Mul2.Mul())