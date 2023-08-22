def three_digit_number():
    sum_of_squares=0
    while number>0:
        digit=number%10
        sum_of_squares+=digit**2
        number//=10
        return sum_of_squares
    
    while True:
        user_input=input("enter a 3-digit number:")
        if user_input.isdigit() and len(user_input)==3:
        number=int(user_input)
        break
    else:
        print("invalid input!please enter a valid 3-digit number:")
        