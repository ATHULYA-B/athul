def remove_vowels(strings):
    vowels=['a','e','i','o','u']
    newlist=[]
    for strings in strings:
        new_strings=([char for char in strings if char not in vowels])
        newlist.append(new_strings)
    return newlist
input_list=['hello','world','python']
output_list=remove_vowels(input_list)
print(output_list)
    

    