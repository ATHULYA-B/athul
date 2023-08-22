def print_upper_words(sentence):
    words=sentence.split()
    for word in words:
        if word[0].isupper():
            print(word)
            
user_input=input("enter a sentence:")
print_upper_words(user_input)