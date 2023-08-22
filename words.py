def count_words(sentence):
    words=sentence.split()
    return len(words)

input_sentence=input("enter a sentence")
word_count=count_words(input_sentence)
print("number of words:",word_count)