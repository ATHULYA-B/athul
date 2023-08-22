class bank():
    def __init__(self,name,accno,bal):
        self.name=name
        self.accountno=accno
        self.bal=bal
    def deposit(self):
        self.amt=int(input("enter amount"))
        self.bal+=self.amt 
        return self.bal
    def withdraw(self):
        self.amt=int(input("enter the amount"))
        self.bal-=self.amt 
        return self.bal
User1=bank("Ken",123,1000)
print(User1.deposit())
print(User1.withdraw())
User2=bank("Aswin",456,1500)
print(User2.deposit())
print(User2.withdraw())
User3=bank("Jolen",789,2000)
print(User3.deposit())
print(User3.withdraw())    
    
        
        
        
        
        
        
                