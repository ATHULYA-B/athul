def is_armstrong(number):
    num_str=str(number)
    num_digits=str(number)
    num_digits=len(num_str)
    armstrong_sum=sum(int(digit)**num_digits for digit in num_str)
    if armstrong_sum==number:
        return True
    else:
        return False
num=int(input("enter a number:"))
if is_armstrong(num):
        print(num,"is an armstrong number:")
else:
        print(num,"is not an armstrong number:")    