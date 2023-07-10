numbers = []
count=0
while count <3:
    number=int(input("enter a number:"))
    numbers.append(number)
    count+=1
    squares=[num**2 for num in numbers]
    squares.sort()
print("squared numbers in reverse order:")
for square in squares:
    print(square)
              
