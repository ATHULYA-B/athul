def find_max_min(lst):
    max_val = lst[0]
    min_val = lst[0]
    
    for num in lst:
        if num > max_val:
         max_val=num
        if num < min_val:
         min_val=num
    return max_val,min_val
my_list=[1,34,5,10,12]
max_value,min_value=find_max_min(my_list)
print("maximum value:",max_value)
print("minimum value:",min_value)
        