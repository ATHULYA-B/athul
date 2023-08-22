import math

class Com():
    def __init__(self,real,imag=0.0):
        self.real=real
        self.imag=imag
        
    def __add__(self,other):
           return complex(self.real + other.real,self.imag + other.imag)
       
    def __sub__(self,other):
           return complex(self.real - other.real, self.imag - other.imag)
       
    def __mul__(self,other):
           return complex(self.real*other.real - self.imag*other.imag, self.imag*other.real + self.real*other.imag)
       
    def __abs__(self):
           return math.sqrt(self).real**2 + self.imag**2
       
    def __neg__(self):
           return complex(-self.real, -self.imag)
       
    def __eq__(self)