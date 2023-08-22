print("Which operation you want to perform\n1.integer to roman\n2.roman to integer:")
i=int(input("enter a choice:"))
if i==1:
    num=int(input("enter a number:"))
    rom=romans(num)
    print(num,"is convereted into",rom.ctor)
elif i==2:class romans():
  
  def __init__(self,num):
      self.num=num
      
      
  def ctor(self):
        if self.num==0:
          return "N"
        elif self.num==1:
          return "I"
        elif self.num==2:
          return "II"
        elif self.num==3:
          return "III"
        elif self.num==4:
          return "IV"
        elif self.num==5:
          return "V"
        elif self.num==6:
          return "VI"
        elif self.num==7:
          return "VII"
        elif self.num==8:
          return "VIII"
        elif self.num==9:
          return "IX"
        elif self.num==10:
          return "X"
      
  def ctor(self):
        if self.num==0:
            return "N"
        elif self.num==1:
            return "I"
        elif self.num==2:
            return "II"
        elif self.num==3:
            return "III"
        elif self.num==4:
            return "IV"
        elif self.num==5:
            return "V"
        elif self.num==6:
            return "VI"
        elif self.num==7:
            return "VII"
        elif self.num==8:
            return "VIII"
        elif self.num==9:
            return "IX"
        elif self.num==10:
            return "X"
        
      

    num2=int(input("enter a roman num:"))
    rom=romans(num2)
    print(num2,"is converted into",rom.ctor)
else:
    print("invalid input")

            
            
         
         
            
            
            
        