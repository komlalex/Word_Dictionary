"""
# Have a python dictionary that has a key-value pair that represents a word and its definition
# collect input from the user, input is a word
# chec if the word is in thhe dictionry
# print the definition of the word
"""
def main():
    word_dictionary = {
        "apple": "a fruit",
        "bible": "the holy book of christians",
        "hi": "a way of greeting",
        "eye": "an organ for seeing",
        "earth": "our plant",
        "python": "a fun programming language"
    }
    
    while True:
        word = input("Enter a word: ")

        if word == "":
         break

        if word in word_dictionary:
            print(f"{word}: {word_dictionary[word]} ")
        else:
           print(f"{word} is not a word in the Alexandrian Dictionary")

main()