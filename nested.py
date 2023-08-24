try:
    
    num=int(input('enter thr numerator'))
    den=int(input('enter the denominator'))
    try:
        result=num/den;
        print('Result=', result)
    except:
        print('divide by zero error')
except:
    print('Invalid Input')
    
print('end of program')