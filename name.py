def initials(name):
    words=name.split()
    capitalized_words=[word.capitalize() for word in words]
    capitalized_name=" ".join(capitalized_words)
    return capitalized_name

name = input("enter your name: ")
capitalized_name=initials(name)
print("Name with initials:", capitalized_name)