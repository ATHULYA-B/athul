def sum_of_squares():
    numbers=[]
    for i in range(3):
      user_input=int(input(f"enter number{i+1}:"))
      numbers.append(user_input)
    sum_of_squares=0
    for num in numbers:
        sum_of_squares+=num**2
    print("the sum of squares of the three numbers is:",sum_of_squares)
sum_of_squares()