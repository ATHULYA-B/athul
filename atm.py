def deposit_amt(amt):
    depo=float(input("enter the amount you want to deposit:"))
    amt=amt+depo
    return amt
def withdraw_amt(amt):
    withd=float(input("enter the amount you want to withdraw:"))
    if(amt>withd):
        amt-=withd
        return amt
    else:
        print("\nInsufficient balance!")
        exit()
        
amount=float(10000)
while (True):
    
        print("\n1.Account Balance \n2.Money Deposit \n3.Money Withdrawal \n4.Exit")
        choice=int(input("enter your choice:"))
        if(choice==1):
           print("Your current bank balance is:",amount)
        elif(choice==2):
           amount = deposit_amt(amount)
           print("Deposit successfully.Your current account balance is",amount)
        elif(choice==3):
           amount = withdraw_amt(amount)
           print("Withdraw successful.Your current account balance is" ,amount)
        elif(choice==4):
            print("Exiting")
            break
        else:
            print('Invalid Input')
    