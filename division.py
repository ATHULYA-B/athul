try:
    a=int(input('enter the first number'))
    b=int(input('enter the second number'))
    
    res=a/b
    print('result=',res)
except(ValueError,TypeError):
    print("Invalid input")
    