def find_longest_word(sentence):
    words=sentence.split()
    longest_word=max(words,key=len)
    return longest_word

input_sentence=input("enter the sentence:")
longest_word=find_longest_word(input_sentence)
print("the longest is:",longest_word)