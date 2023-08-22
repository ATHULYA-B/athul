def count_occurence(string,character):
    count=0
    for char in string:
        if char == character:
            count += 1
    return count
string=input("enter a string:")
character=input("enter a character:")
occurence=count_occurence(string,character)
print("the character ",character," appears ",occurence," times in the string.")