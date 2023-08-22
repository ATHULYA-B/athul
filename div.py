class Calc():
    def __init__(self,n,m):
        self.num1=n
        self.num2=m
    def Div(self):
        self.sum=self.num1/self.num2
        return self.sum
Div1=Calc(10,20)
print(Div1.Div())
Div2=Calc(20,15)
print(Div2.Div())